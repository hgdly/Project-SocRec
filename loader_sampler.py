#--------Imports-----------------------------------------------------------------------------------

import scipy.io as sio
import pandas as pd
import numpy as np

from icecream import ic

#--------Constants---------------------------------------------------------------------------------

EPINIONS_FOLDER_PATH = "epinions/"
EPINIONS_TRUST_PATH = f"{EPINIONS_FOLDER_PATH}trustnetwork.mat"
EPINIONS_RATINGS_PATH = f"{EPINIONS_FOLDER_PATH}rating.mat"

DELICIOUS_FOLDER_PATH = "delicious/"
DELICIOUS_TRUST_PATH = f"{DELICIOUS_FOLDER_PATH}user_contacts-timestamps.dat"
DELICIOUS_RATINGS_PATH = f"{DELICIOUS_FOLDER_PATH}user_taggedbookmarks-timestamps.dat"

SAMPLE_SIZE = 2000

#--------Classes-----------------------------------------------------------------------------------

class LoaderSaver:
    """Class for loading data from .mat and .dat files and saving it to .txt files."""

    def __init__(self):
        """Constructor."""
        pass

    def load_mat_file(self, filename, column_to_select, original_columns, columns_to_drop):
        """Load data from .mat file."""

        data = sio.loadmat(filename)
        data = data[column_to_select]
        data = pd.DataFrame(data)
        data.columns = original_columns
        return data.drop(columns_to_drop, axis=1)
    
    def load_dat_file(self, filename, dict_to_rename):
        """Load data from .dat file."""

        data = pd.read_csv(filename, sep='\t')
        data = data.drop(['timestamp'], axis=1)
        return data.rename(columns=dict_to_rename)
    
    def group_normalize(self, data):
        """For Delicious dataset, group by [user, item] and normalize the ratings between 0 and 5."""

        data = data.groupby(['user', 'item']).size().reset_index(name='rating')
        data['rating'] = data['rating'].apply(lambda x: x*5/ data['rating'].max())
        return data
    
    def add_weights(self, data):
        """Add weights to the edges of an unweighted graph."""

        data['weight'] = 1
        return data
    
    def loader(self):
        """Load data from files."""

        epinions_trust = self.load_mat_file(EPINIONS_TRUST_PATH, 'trustnetwork', ['user1', 'user2'], [])
        epinions_ratings = self.load_mat_file(EPINIONS_RATINGS_PATH, 'rating', ['user', 'item', 'category', 'rating'], ['category'])

        delicious_trust = self.load_dat_file(DELICIOUS_TRUST_PATH, {'userID': 'user1', 'contactID': 'user2'})
        delicious_ratings = self.load_dat_file(DELICIOUS_RATINGS_PATH, {'userID': 'user', 'bookmarkID': 'item'})

        delicious_ratings = self.group_normalize(delicious_ratings)
        epinions_trust = self.add_weights(epinions_trust)
        delicious_trust = self.add_weights(delicious_trust)

        return epinions_trust, epinions_ratings, delicious_trust, delicious_ratings
    
    def save_to_txt(self, data, filename):
        """Save data to .txt file."""

        data.to_csv(filename, sep=' ', index=False, header=False)

    def saver(self, epinions_trust, epinions_ratings, delicious_trust, delicious_ratings):
        """Save data to files."""

        self.save_to_txt(epinions_trust, f"{EPINIONS_FOLDER_PATH}ep_trust.txt")
        self.save_to_txt(epinions_ratings, f"{EPINIONS_FOLDER_PATH}ep_ratings.txt")
        self.save_to_txt(delicious_trust, f"{DELICIOUS_FOLDER_PATH}dl_trust.txt")
        self.save_to_txt(delicious_ratings, f"{DELICIOUS_FOLDER_PATH}dl_ratings.txt")
    
class Sampler:
    """Class for sampling data."""

    def __init__(self):
        """Constructor."""
        pass

    def sample(self, trust_data, ratings_data):
        """Sample data with SAMPLE_SIZE users."""

        users = trust_data['user1'].unique()
        users = np.random.choice(users, size=SAMPLE_SIZE if len(users) > SAMPLE_SIZE else len(users), replace=False)
        # Keep only the data of the sampled users
        trust_data = trust_data[trust_data['user1'].isin(users)]
        trust_data = trust_data[trust_data['user2'].isin(users)]
        ratings_data = ratings_data[ratings_data['user'].isin(users)]
        return trust_data, ratings_data

#--------Functions---------------------------------------------------------------------------------

def main():
    """Main function of the program."""
    
    loader_saver = LoaderSaver()
    sampler = Sampler()

    epinions_trust, epinions_ratings, delicious_trust, delicious_ratings = loader_saver.loader()
    epinions_trust, epinions_ratings = sampler.sample(epinions_trust, epinions_ratings)
    delicious_trust, delicious_ratings = sampler.sample(delicious_trust, delicious_ratings)
    loader_saver.saver(epinions_trust, epinions_ratings, delicious_trust, delicious_ratings)

#--------Execution---------------------------------------------------------------------------------

if __name__ == "__main__":
    main()