def hash(s):
    return sum((ord(ch) * 17) % 256 for ch in s)

boxes = [[] for _ in range(256)]
focal_len = {}

for instruction in open(0).read().strip().split(","):
    if "-" in instruction:
        label = instruction[:-1]
        index = hash(label)
        if label in boxes[index]:
            boxes[index].remove(label)
    else:
        label, length = instruction.split("=")
        length = int(length)
        
        index = hash(label)
        if label not in boxes[index]:
            boxes[index].append(label)
            
        focal_len[label] = length

print(sum(box_number * lens_slot * focal_len[label] for box_number, box in enumerate(boxes, 1) for lens_slot, label in enumerate(box, 1)))