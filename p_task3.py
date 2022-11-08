
import sys

with open(sys.argv[1], 'r') as f:

    user_agent_dict = {}

    for line in f:

        line_list = line.split()
        try:
            user_agent = line_list[11]
        except:
            pass

        if user_agent in user_agent_dict:
            user_agent_dict[user_agent] += 1

        else:
            user_agent_dict[user_agent] = 1

    print("Total number of different user agents: {}".format(len(user_agent_dict)))

    for key, value in user_agent_dict.items():
        print("{}: {}".format(key, value))
        

