import os

def process_domains(input_file, output_file):
    print(f"Checking if input file exists: {input_file}")
    if not os.path.exists(input_file):
        print("Input file does not exist!")
        return
    
    print("Reading input file...")
    try:
        with open(input_file, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        print(f"Read {len(lines)} lines from input file.")
    except Exception as e:
        print(f"Error reading input file: {e}")
        return
    
    # Process lines: strip whitespace, wrap in single quotes, and filter out empty lines
    processed_lines = ["'{}'".format(line.strip()) for line in lines if line.strip()]
    print(f"Processed {len(processed_lines)} non-empty lines.")
    
    # Join with commas
    result = ','.join(processed_lines)
    print(f"Joined lines into a string of {len(result)} characters.")
    
    # Write to output file
    print(f"Writing to output file: {output_file}")
    try:
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(result)
        print("Writing complete.")
    except Exception as e:
        print(f"Error writing output file: {e}")
        return

if __name__ == "__main__":
    input_file = r'c:\Users\nasAdmin\git\CN-Malicious-website-list\DNS-BH 恶意软件域过滤清单.txt'
    output_file = r'c:\Users\nasAdmin\git\CN-Malicious-website-list\核心屏蔽2025.txt'
    process_domains(input_file, output_file)
    print("Processing complete. Output written to", output_file)