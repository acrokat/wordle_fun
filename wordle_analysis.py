if __name__ == '__main__':
    # read in dict of past responses
    with open('./old_answers.txt', 'r') as file:
        content = file.read()
        words = content.split()
        print(words[:10])
    