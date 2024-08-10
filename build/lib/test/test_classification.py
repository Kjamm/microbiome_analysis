import unittest
from microbiome_analysis import classification

class TestClassification(unittest.TestCase):

    def setUp(self):
        self.sequences = [
            'ATCGGCTAAG',
            'GCTTAGCTAG',
            'TTCGCTGATC',
            'GCTAGCTAGT'
        ]

        self.labels = [
            'species_1',
            'species_2',
            'species_1',
            'species_2'
        ]

        self.new_samples = [
            'ATCGGCTAAG',
            'GCTAGCTAGT'
        ]

        self.trained_classifier = classification.train_classifier(self.sequences, self.labels)

    def test_classify_sequences(self):
        predictions = classification.classify_sequences(self.new_samples, self.trained_classifier)
        self.assertIsNotNone(predictions)
        self.assertEqual(len(predictions), 2)

    def test_train_classifier(self):
        classifier = classification.train_classifier(self.sequences, self.labels)
        self.assertIsNotNone(classifier)

    def test_classify_new_samples(self):
        predictions = classification.classify_new_samples(self.new_samples, self.trained_classifier)
        self.assertIsNotNone(predictions)
        self.assertEqual(len(predictions), 2)

if __name__ == '__main__':
    unittest.main()
