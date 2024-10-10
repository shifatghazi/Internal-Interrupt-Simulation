import re

#MUST MANUALLY COPY AND PASTE execution text file here
log_data = """
0, 29, CPU execution
29, 1, switch to kernel mode
30, 3, context saved
33, 1, find vector 3 in memory position 0x0006
34, 1, load address 0X042B into the PC
35, 143, SYSCALL: run the ISR
178, 95, transfer data
273, 49, check for errors
322, 1, IRET
323, 89, CPU execution
412, 1, check priority of interrupt
413, 1 , check if masked
414, 1, switch to kernel mode
415, 3, context saved
418, 1, find vector 17 in memory position 2204X
419, 1, load address 0X05B3 into the PC
420, 241, END_IO
661, 1, IRET
662, 32, CPU execution
694, 1, switch to kernel mode
695, 3, context saved
698, 1, find vector 10 in memory position 0x0014
699, 1, load address 0X07B0 into the PC
700, 95, SYSCALL: run the ISR
795, 63, transfer data
858, 32, check for errors
890, 1, IRET
891, 53, CPU execution
944, 1, check priority of interrupt
945, 1 , check if masked
946, 1, switch to kernel mode
947, 3, context saved
950, 1, find vector 23 in memory position 2e04X
951, 1, load address 0X028C into the PC
952, 209, END_IO
1161, 1, IRET
1162, 72, CPU execution
1234, 1, switch to kernel mode
1235, 2, context saved
1237, 1, find vector 5 in memory position 0x000A
1238, 1, load address 0X048B into the PC
1239, 2365,107, SYSCALL: run the ISR
1346, 71, transfer data
1417, 36, check for errors
1453, 1, IRET
1454, 60, CPU execution
1514, 1, check priority of interrupt
1515, 1 , check if masked
1516, 1, switch to kernel mode
1517, 3, context saved
1520, 1, find vector 17 in memory position 2204X
1521, 1, load address 0X05B3 into the PC
1522, 181, END_IO
1703, 1, IRET
1704, 33, CPU execution
1737, 1, switch to kernel mode
1738, 2, context saved
1740, 1, find vector 8 in memory position 0x0010
1741, 1, load address 0X06EF into the PC
1742, 137, SYSCALL: run the ISR
1879, 91, transfer data
1970, 46, check for errors
2016, 1, IRET
2017, 43, CPU execution
2060, 1, check priority of interrupt
2061, 1 , check if masked
2062, 1, switch to kernel mode
2063, 3, context saved
2066, 1, find vector 21 in memory position 2a04X
2067, 1, load address 0X0523 into the PC
2068, 297, END_IO
 1, IRET
2366, 22, CPU execution
2388, 1, switch to kernel mode
2389, 3, context saved
2392, 1, find vector 7 in memory position 0x000E
2393, 1, load address 0X00BD into the PC
2394, 77, SYSCALL: run the ISR
2471, 51, transfer data
2522, 27, check for errors
2549, 1, IRET
2550, 98, CPU execution
2648, 1, check priority of interrupt
2649, 1 , check if masked
2650, 1, switch to kernel mode
2651, 3, context saved
2654, 1, find vector 18 in memory position 2404X
2655, 1, load address 0X060A into the PC
2656, 184, END_IO
2840, 1, IRET
2841, 55, CPU execution
2896, 1, switch to kernel mode
2897, 2, context saved
2899, 1, find vector 9 in memory position 0x0012
2900, 1, load address 0X036C into the PC
2901, 60, SYSCALL: run the ISR
2961, 40, transfer data
3001, 20, check for errors
3021, 1, IRET
3022, 74, CPU execution
3096, 1, check priority of interrupt
3097, 1 , check if masked
3098, 1, switch to kernel mode
3099, 3, context saved
3102, 1, find vector 21 in memory position 2a04X
3103, 1, load address 0X0523 into the PC
3104, 284, END_IO
3388, 1, IRET
3389, 55, CPU execution
3444, 1, switch to kernel mode
3445, 1, context saved
3446, 1, find vector 3 in memory position 0x0006
3447, 1, load address 0X042B into the PC
3448, 163, SYSCALL: run the ISR
3611, 108, transfer data
3719, 55, check for errors
3774, 1, IRET
3775, 37, CPU execution
3812, 1, check priority of interrupt
3813, 1 , check if masked
3814, 1, switch to kernel mode
3815, 3, context saved
3818, 1, find vector 20 in memory position 2804X
3819, 1, load address 0X07B7 into the PC
3820, 366, END_IO
4186, 1, IRET
4187, 100, CPU execution
4287, 1, switch to kernel mode
4288, 1, context saved
4289, 1, find vector 15 in memory position 0x001E
4290, 1, load address 0X0584 into the PC
4291, 155, SYSCALL: run the ISR
4446, 103, transfer data
4549, 52, check for errors
4601, 1, IRET
4602, 54, CPU execution
4656, 1, check priority of interrupt
4657, 1 , check if masked
4658, 1, switch to kernel mode
4659, 3, context saved
4662, 1, find vector 23 in memory position 2e04X
4663, 1, load address 0X028C into the PC
4664, 380, END_IO
5044, 1, IRET
5045, 90, CPU execution
5135, 1, switch to kernel mode
5136, 2, context saved
5138, 1, find vector 5 in memory position 0x000A
5139, 1, load address 0X048B into the PC
5140, 56, SYSCALL: run the ISR
5196, 37, transfer data
5233, 19, check for errors
5252, 1, IRET
5253, 50, CPU execution
5303, 1, check priority of interrupt
5304, 1 , check if masked
5305, 1, switch to kernel mode
5306, 3, context saved
5309, 1, find vector 17 in memory position 2204X
5310, 1, load address 0X05B3 into the PC
5311, 148, END_IO
5459, 1, IRET
5460, 94, CPU execution
5554, 1, switch to kernel mode
5555, 3, context saved
5558, 1, find vector 14 in memory position 0x001C
5559, 1, load address 0X0165 into the PC
5560, 53, SYSCALL: run the ISR
5613, 35, transfer data
5648, 19, check for errors
5667, 1, IRET
5668, 80, CPU execution
5748, 1, check priority of interrupt
5749, 1 , check if masked
5750, 1, switch to kernel mode
5751, 3, context saved
5754, 1, find vector 21 in memory position 2a04X
5755, 1, load address 0X0523 into the PC
5756, 268, END_IO
6024, 1, IRET
6025, 33, CPU execution
6058, 1, switch to kernel mode
6059, 3, context saved
6062, 1, find vector 3 in memory position 0x0006
6063, 1, load address 0X042B into the PC
6064, 75, SYSCALL: run the ISR
6139, 50, transfer data
6189, 25, check for errors
6214, 1, IRET
6215, 80, CPU execution
6295, 1, check priority of interrupt
6296, 1 , check if masked
6297, 1, switch to kernel mode
6298, 3, context saved
6301, 1, find vector 20 in memory position 2804X
6302, 1, load address 0X07B7 into the PC
6303, 336, END_IO
6639, 1, IRET
6640, 46, CPU execution
6686, 1, switch to kernel mode
6687, 3, context saved
6690, 1, find vector 11 in memory position 0x0016
6691, 1, load address 0X01F8 into the PC
6692, 69, SYSCALL: run the ISR
6761, 46, transfer data
6807, 23, check for errors
6830, 1, IRET
6831, 75, CPU execution
6906, 1, check priority of interrupt
6907, 1 , check if masked
6908, 1, switch to kernel mode
6909, 3, context saved
6912, 1, find vector 25 in memory position 3204X
6913, 1, load address 0X05D3 into the PC
6914, 202, END_IO
7116, 1, IRET
7117, 10, CPU execution
7127, 1, switch to kernel mode
7128, 2, context saved
7130, 1, find vector 5 in memory position 0x000A
7131, 1, load address 0X048B into the PC
7132, 178, SYSCALL: run the ISR
7310, 118, transfer data
7428, 60, check for errors
7488, 1, IRET
7489, 92, CPU execution
7581, 1, check priority of interrupt
7582, 1 , check if masked
7583, 1, switch to kernel mode
7584, 3, context saved
7587, 1, find vector 17 in memory position 2204X
7588, 1, load address 0X05B3 into the PC
7589, 243, END_IO
7832, 1, IRET
7833, 70, CPU execution
7903, 1, switch to kernel mode
7904, 1, context saved
7905, 1, find vector 13 in memory position 0x001A
7906, 1, load address 0X06C7 into the PC
7907, 84, SYSCALL: run the ISR
7991, 56, transfer data
8047, 28, check for errors
8075, 1, IRET
8076, 82, CPU execution
8158, 1, check priority of interrupt
8159, 1 , check if masked
8160, 1, switch to kernel mode
8161, 3, context saved
8164, 1, find vector 23 in memory position 2e04X
8165, 1, load address 0X028C into the PC
8166, 392, END_IO
8558, 1, IRET
8559, 100, CPU execution
8659, 1, switch to kernel mode
8660, 2, context saved
8662, 1, find vector 5 in memory position 0x000A
8663, 1, load address 0X048B into the PC
8664, 87, SYSCALL: run the ISR
8751, 58, transfer data
8809, 30, check for errors
8839, 1, IRET
8840, 74, CPU execution
8914, 1, check priority of interrupt
8915, 1 , check if masked
8916, 1, switch to kernel mode
8917, 3, context saved
8920, 1, find vector 17 in memory position 2204X
8921, 1, load address 0X05B3 into the PC
8922, 345, END_IO
9267, 1, IRET
9268, 75, CPU execution
9343, 1, switch to kernel mode
9344, 3, context saved
9347, 1, find vector 15 in memory position 0x001E
9348, 1, load address 0X0584 into the PC
9349, 116, SYSCALL: run the ISR
9465, 77, transfer data
9542, 40, check for errors
9582, 1, IRET
9583, 56, CPU execution
9639, 1, check priority of interrupt
9640, 1 , check if masked
9641, 1, switch to kernel mode
9642, 3, context saved
9645, 1, find vector 20 in memory position 2804X
9646, 1, load address 0X07B7 into the PC
9647, 104, END_IO
9751, 1, IRET
9752, 97, CPU execution
9849, 1, switch to kernel mode
9850, 2, context saved
9852, 1, find vector 6 in memory position 0x000C
9853, 1, load address 0X0639 into the PC
9854, 89, SYSCALL: run the ISR
9943, 59, transfer data
10002, 31, check for errors
10033, 1, IRET
10034, 29, CPU execution
10063, 1, check priority of interrupt
10064, 1 , check if masked
10065, 1, switch to kernel mode
10066, 3, context saved
10069, 1, find vector 18 in memory position 2404X
10070, 1, load address 0X060A into the PC
10071, 172, END_IO
10243, 1, IRET
10244, 73, CPU execution
10317, 1, switch to kernel mode
10318, 3, context saved
10321, 1, find vector 15 in memory position 0x001E
10322, 1, load address 0X0584 into the PC
10323, 103, SYSCALL: run the ISR
10426, 69, transfer data
10495, 35, check for errors
10530, 1, IRET
10531, 75, CPU execution
10606, 1, check priority of interrupt
10607, 1 , check if masked
10608, 1, switch to kernel mode
10609, 3, context saved
10612, 1, find vector 22 in memory position 2c04X
10613, 1, load address 0X03B7 into the PC
10614, 134, END_IO
10748, 1, IRET
10749, 48, CPU execution
10797, 1, switch to kernel mode
10798, 1, context saved
10799, 1, find vector 7 in memory position 0x000E
10800, 1, load address 0X00BD into the PC
10801, 143, SYSCALL: run the ISR
10944, 95, transfer data
11039, 48, check for errors
11087, 1, IRET
11088, 16, CPU execution
11104, 1, check priority of interrupt
11105, 1 , check if masked
11106, 1, switch to kernel mode
11107, 3, context saved
11110, 1, find vector 18 in memory position 2404X
11111, 1, load address 0X060A into the PC
11112, 171, END_IO
11283, 1, IRET
11284, 58, CPU execution
11342, 1, switch to kernel mode
11343, 1, context saved
11344, 1, find vector 11 in memory position 0x0016
11345, 1, load address 0X01F8 into the PC
11346, 172, SYSCALL: run the ISR
11518, 114, transfer data
11632, 58, check for errors
11690, 1, IRET
11691, 31, CPU execution
11722, 1, check priority of interrupt
11723, 1 , check if masked
11724, 1, switch to kernel mode
11725, 3, context saved
11728, 1, find vector 24 in memory position 3004X
11729, 1, load address 0X05E8 into the PC
11730, 189, END_IO
11919, 1, IRET
11920, 65, CPU execution
11985, 1, switch to kernel mode
11986, 1, context saved
11987, 1, find vector 3 in memory position 0x0006
11988, 1, load address 0X042B into the PC
11989, 182, SYSCALL: run the ISR
12171, 121, transfer data
12292, 61, check for errors
12353, 1, IRET
12354, 91, CPU execution
12445, 1, check priority of interrupt
12446, 1 , check if masked
12447, 1, switch to kernel mode
12448, 3, context saved
12451, 1, find vector 16 in memory position 2004X
12452, 1, load address 0X02DF into the PC
12453, 193, END_IO
12646, 1, IRET
12647, 69, CPU execution
12716, 1, switch to kernel mode
12717, 1, context saved
12718, 1, find vector 14 in memory position 0x001C
12719, 1, load address 0X0165 into the PC
12720, 109, SYSCALL: run the ISR
12829, 73, transfer data
12902, 37, check for errors
12939, 1, IRET
12940, 60, CPU execution
13000, 1, check priority of interrupt
13001, 1 , check if masked
13002, 1, switch to kernel mode
13003, 3, context saved
13006, 1, find vector 22 in memory position 2c04X
13007, 1, load address 0X03B7 into the PC
13008, 206, END_IO
13214, 1, IRET
13215, 64, CPU execution
"""

# Function to parse the log data and return a list of (duration, event description)
def parse_log_data(log_data):
    log_entries = []
    
    # Use regex to match lines of the form: time, duration, description
    pattern = r"(\d+),\s+(\d+),\s+(.+)"
    
    for match in re.finditer(pattern, log_data):
        duration = int(match.group(2))
        event = match.group(3).strip()
        log_entries.append((duration, event))
    
    return log_entries

# Call the function to parse the data
log_entries = parse_log_data(log_data)


# Initialize variables for total times
cpu_time = 0
io_time = 0
overhead_time = 0


# Categorize the times based on manual data entry
for duration, event in log_entries:
    if "CPU execution" in event or "SYSCALL" in event:
        cpu_time += duration
    elif "transfer data" in event or "check for errors" in event or "END_IO" in event:
        io_time += duration
    else:
        overhead_time += duration

# Total time
total_time = cpu_time + io_time + overhead_time

# Calculate the ratios
if total_time > 0:
    cpu_ratio = (cpu_time / total_time) * 100
    io_ratio = (io_time / total_time) * 100
    overhead_ratio = (overhead_time / total_time) * 100
else:
    cpu_ratio = io_ratio = overhead_ratio = 0

# Print results
print(f"CPU Time: {cpu_time} ms, Ratio: {cpu_ratio:.2f}%")
print(f"I/O Time: {io_time} ms, Ratio: {io_ratio:.2f}%")
print(f"Overhead Time: {overhead_time} ms, Ratio: {overhead_ratio:.2f}%")