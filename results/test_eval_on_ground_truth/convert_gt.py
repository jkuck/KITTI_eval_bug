import glob


if __name__ == "__main__":
    for cur_gt_file in glob.iglob("./label_02/*"): 
        seq_name = cur_gt_file.split("/")[2]
        gt_f = open(cur_gt_file, "r") 
        gt_as_result = open("./data/" + seq_name, "w")

        dontCareIdx = 999999 #larger than any real index
        for line in gt_f:
            fields = line.split(" ")
            writeLine = False
            if fields[2] == 'DontCare':
                target_id = dontCareIdx
                dontCareIdx += 1 #avoid assigning the same id to multiple targets in the same frame
                writeLine = True
            elif fields[2] == 'Car':
                target_id = int(fields[1])
                writeLine = True
            if writeLine:
                gt_as_result.write( "%s %d Car -1 -1 2.57 %s %s %s %s -1 -1 -1 -1000 -1000 -1000 -10 1\n" % \
                        (fields[0], target_id, fields[6], fields[7], fields[8], fields[9]))

        gt_as_result.close()    
        gt_f.close()

