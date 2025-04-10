class AverageFilter:
    def __init__(self, sample_size):
        self.sample_size = sample_size
        self.samples = []

    def add_sample(self, sample):
        if len(self.samples) >= self.sample_size:
            self.samples.pop(0)
        self.samples.append(sample)

    def calculate_average(self):
        if not self.samples:
            return 0
        return sum(self.samples) / len(self.samples)