filename = input("Enter the file name: ")

try:
    with open(filename, "r") as file:
        total_confidence = 0
        count = 0

        for line in file:
            if line.startswith("X-DSPAM-Confidence:"):
                parts = line.split(":")
                try:
                    confidence = float(parts[1].strip())  # Convert to float
                    total_confidence += confidence
                    count += 1
                except ValueError:
                    print("Skipping invalid confidence value:", parts[1].strip())

        if count > 0:
            average_confidence = total_confidence / count
            print("Average spam confidence:", average_confidence)
        else:
            print("No spam confidence lines found in the file.")

except FileNotFoundError:
    print("File not found. Please check the filename and try again.")
