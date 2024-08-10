import unittest
import os
from microbiome_analysis import preprocessing

class TestPreprocessing(unittest.TestCase):

    def setUp(self):
        self.example_fastq = os.path.join(os.path.dirname(__file__), 'example.fastq')

    def test_read_sequences(self):
        sequences = preprocessing.read_fastq(self.example_fastq)
        self.assertGreater(len(sequences), 0)

    def test_quality_filter(self):
        sequences = preprocessing.read_fastq(self.example_fastq)
        # Assuming we have a quality_filter function, here's a mock implementation
        filtered_sequences = [seq for seq in sequences if min(seq.letter_annotations["phred_quality"]) >= 20 and len(seq) >= 30]
        self.assertGreater(len(filtered_sequences), 0)

if __name__ == '__main__':
    unittest.main()
