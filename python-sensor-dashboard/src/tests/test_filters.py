def test_average_filter():
    from app.utils.filters import AverageFilter

    # Test case 1: Basic functionality
    filter = AverageFilter(sample_size=3)
    filter.add_sample(10)
    filter.add_sample(20)
    assert filter.calculate_average() == 15.0

    # Test case 2: Exceeding sample size
    filter.add_sample(30)
    filter.add_sample(40)  # This should remove the first sample (10)
    assert filter.calculate_average() == 30.0

    # Test case 3: Check with fewer samples than sample size
    filter = AverageFilter(sample_size=5)
    filter.add_sample(10)
    filter.add_sample(20)
    assert filter.calculate_average() == 15.0  # Average of 10 and 20

    # Test case 4: All samples the same
    filter = AverageFilter(sample_size=3)
    filter.add_sample(5)
    filter.add_sample(5)
    filter.add_sample(5)
    assert filter.calculate_average() == 5.0

    # Test case 5: No samples added
    filter = AverageFilter(sample_size=3)
    assert filter.calculate_average() == 0.0  # Should handle no samples gracefully