from selenium import webdriver

base_url = "http://drr.land.gov.bd/khatian/"

print("Enter search starting point : ")
suffix_from = int(input())
print("Enter search starting point : ")
suffix_to = int(input())
print("Enter search filter string : ")
search_string = input()

# suffix_from = 15654000
# suffix_to = 15654100
# search_string = "নীলফামারী টাউন"

driver = webdriver.Firefox()
f = open("khotian_output.txt", "a")

for suff in range(suffix_from, suffix_to, 1):
    try_url = base_url + str(suff)
    driver.get(try_url)
    khotian_body = driver.find_element_by_xpath("/html/body")
    print(khotian_body.text)

    if search_string in khotian_body.text:
        f.write("\n\nUrl : {} \n\n".format(try_url))
        f.write("Khotian Data :\n\n {} \n".format(khotian_body.text))
        f.write("\n--------------------------------------------------------------------------------------------\n\n\n")

f.close()
driver.close()
