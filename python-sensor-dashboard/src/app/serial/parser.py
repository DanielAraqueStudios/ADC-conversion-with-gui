class DataParser:
    def __init__(self):
        self.data_buffer = ""

    def parse(self, raw_data):
        self.data_buffer += raw_data
        lines = self.data_buffer.splitlines()
        parsed_data = []

        for line in lines:
            if line.startswith("TEMP:"):
                try:
                    temp_value = float(line.split(":")[1])
                    parsed_data.append(("temperature", temp_value))
                except ValueError:
                    continue
            elif line.startswith("PESO:"):
                try:
                    weight_value = float(line.split(":")[1])
                    parsed_data.append(("weight", weight_value))
                except ValueError:
                    continue

        self.data_buffer = lines[-1] if lines else ""
        return parsed_data

    def clear_buffer(self):
        self.data_buffer = ""