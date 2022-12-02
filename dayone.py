import sys

data_file = "./data/dayone.dat"
locations = [1] # have to have a start point

def sum_of_list(list, size):
    """
    Recursive way of summing a list
    """
    if (size == 0):
        return 0
    else:
        return list[size - 1] + sum_of_list(list, size - 1)

def sum_extract(items):
        """
        Sum the list, after removing carriage returns
        """
        cleaned = [int(x.rstrip()) for x in items]
        result = sum_of_list(cleaned,len(cleaned))
        return result

def main():

    highest_score = 0
    all_scores = []

    with open(data_file, 'r') as f:
        data_lines = f.readlines()

    for n, value in enumerate(data_lines,1):  # Marking all the gaps in the data file
        if value == '\n':
            locations.append(n)

    print(f"{data_file} Contains {len(data_lines)} lines of data, comprising of {len(locations)} data sets")

    max = 260
    set = 1
    for i in range(0,len(locations),1):

        a = locations[i]

        try: # adjust for the end
            b = locations[i+1]
            to_val = b -1
        except IndexError as error:
            b = len(data_lines)+1 
            to_val = b

        if a == 1: # adjust for the start
            from_val = 0
        else:
            from_val = a

        results = sum_extract(data_lines[from_val:to_val])
        all_scores.append(results)

        if results >= highest_score:
            highest_score = results

        print (f"set {set}) {a}-{b} {results}")
        set += 1

        if set > max:
            print(f"Highest score is {highest_score}")
            all_scores.sort(reverse=True)
            print(f"Top 3 {all_scores[:3]}")
            print(f"Totals up to: {sum_of_list(all_scores[:3],len(all_scores[:3]))}")

if __name__ == "__main__":
    main()


