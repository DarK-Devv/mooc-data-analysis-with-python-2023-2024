import unittest
import pandas a
from io import StringIO
from fossil_analysis import (
    download_and_load_data,
    clean_data,
    assign_time_units,
    assign_species_ids,
    remove_duplicates,
    analyze_occurrences,
    sampling_analysis,
    logistic_regression,
    calculate_significance
)

class TestFossilAnalysis(unittest.TestCase):

    def setUp(self):
        # Create sample data as a string (simulating a CSV file)
        data = """LIDNUM,LAT,LONG,MIN_AGE,MAX_AGE,SPECIES,GENUS,CONTINENT
        Loc1,40.7128,-74.0060,10,15,Tyrannosaurus,Tyrannosaurus,North America
        Loc2,34.0522,-118.2437,5,10,Triceratops,Triceratops,North America
        Loc3,51.5074,-0.1278,15,20,Stegosaurus,Stegosaurus,Europe
        Loc4,-33.8688,151.2093,10,15,Brachiosaurus,Brachiosaurus,Australia
        Loc5,-22.9068,-43.1729,5,10,Allosaurus,Allosaurus,South America
        """
        # Load the sample data into a DataFrame
        self.df = pd.read_csv(StringIO(data))

    def test_download_and_load_data(self):
        df = download_and_load_data(StringIO(data))
        self.assertEqual(len(df), 5)  # Check if the correct number of rows is loaded

    def test_clean_data(self):
        cleaned_df = clean_data(self.df)
        self.assertEqual(len(cleaned_df), 5)  # Ensure no rows are removed in cleaning process

    def test_assign_time_units(self):
        df_with_time_units = assign_time_units(self.df)
        self.assertTrue('TIME_UNIT' in df_with_time_units.columns)  # Check if TIME_UNIT column is added

    def test_assign_species_ids(self):
        df_with_species_ids = assign_species_ids(self.df)
        self.assertTrue('SPECIES_ID' in df_with_species_ids.columns)  # Check if SPECIES_ID column is added

    def test_remove_duplicates(self):
        df_without_duplicates = remove_duplicates(self.df)
        self.assertEqual(len(df_without_duplicates), 5)  # Ensure no duplicate rows are removed

    def test_analyze_occurrences(self):
        occurrences = analyze_occurrences(self.df)
        self.assertEqual(len(occurrences), 1)  # Check if only one TIME_UNIT is analyzed in this test case

    def test_sampling_analysis(self):
        sampling = sampling_analysis(self.df)
        self.assertEqual(len(sampling), 4)  # Assuming there are 4 continents in the sample data

    def test_logistic_regression(self):
        result = logistic_regression(self.df)
        self.assertIsNotNone(result)  # Check if logistic regression model is successfully fitted

    def test_calculate_significance(self):
        result = logistic_regression(self.df)
        significance_df = calculate_significance(self.df, result)
        self.assertEqual(len(significance_df), 5)  # Assuming there are 5 localities in the sample data

if __name__ == '__main__':
    unittest.main()

