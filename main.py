import pandas as pd
from user_agents import parse  # !pip install user-agents
from collections import Counter

# 01 - IMPORT FILES
df = pd.read_csv('./user_agent_date.csv', sep='\t', header=None)

# 02 - PROCESS DATA

# convert to list to iterate easily
raw_list = df.values.tolist()

# init restult variables
user_agents_browsers = []
user_agents_browsers_family = []
is_mobile = 0
is_tablet = 0
is_desktop = 0
is_bot = 0

# iterate over raw user agent list to get browser details
for ua_string in raw_list:
    user_agent = parse(str(ua_string))
    if user_agent.is_mobile:
        is_mobile = is_mobile + 1

    if user_agent.is_tablet:
        is_tablet = is_tablet + 1

    if user_agent.is_pc:
        is_desktop = is_desktop + 1

    if user_agent.is_bot:
        is_bot = is_bot + 1

    # Append Browser to user agent list
    user_agents_browsers.append(user_agent.browser)

    # Append browser family
    user_agents_browsers_family.append(user_agent.browser.family)


# count user agents browser families
count_family = Counter(user_agents_browsers_family)
count_browsers = Counter(user_agents_browsers)


# 03 - PRINT RESULTS & OUTPUT TO TEXT
text_file = open("Output.txt", "w")

text_file.write("{} user agent requests analyzed \n".format(
    len(user_agents_browsers)))
text_file.write("Mobile : {} \n".format(is_mobile))
text_file.write("Tablet : {} \n".format(is_tablet))
text_file.write("Desktop : {} \n".format(is_desktop))
text_file.write("Bots : {} \n".format(is_bot))

text_file.write("\nHere are the 50 most common Browsers by Family : \n")
text_file.write(str(count_family.most_common(50)))

text_file.write("\nHere are the 100 most common Browsers with version detail : \n")
text_file.write(str(count_browsers.most_common(100)))

text_file.close()
