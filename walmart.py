# Danielle Crosswell
# L2 Technology Intern Coding Challenge
# December 2015

import urllib.request as ur
import json
import csv

def main():
    
    #create csv file
    with open('data.csv', 'w', newline='') as csvfile:
        csvwrite = csv.writer(csvfile, dialect='excel')
        csvwrite.writerow(['Search Term: Cereal'] + [' ']*4)
        csvwrite.writerow(['Brand'] + ['Cereal Name'] 
                          + ['Rating'] + ['Search Ranking']
                          + ['Num of Reviews']) 

        apiKey = 'kp57gxkz4eh8q9kqn72cf5am' #provided API Key
        
        #Create list to hold info about each brand
        #brand = [num of searches: cereal, top 3: cereal, num of 
        #         searches: cold cereal, top 3: cold cereal]
        ch_list = [0,0,0,0]
        ka_list = [0,0,0,0]
        ke_list = [0,0,0,0]
        po_list = [0,0,0,0]

        #Gather data of "cereal" search term
        start = 1
        #URI for searching for cereal
        URI = ('http://api.walmartlabs.com/v1/search?start=' + str(start) 
               + '&numItems=25&query=cereal&format=json&apiKey=' + apiKey)
        response = ur.urlopen(URI)
        html = response.read().decode('utf-8')
        result = json.loads(html)
            
        search_num = 1
        totalResults = result['totalResults']
        start += 25
        while (start <= totalResults and start <= 1000): #pagination limit is top 1000 items
            max = result['numItems']
            for i in range(0,max):
               	#check brand
                id = str(result['items'][i]['itemId'])
                URI_lookup = ('http://api.walmartlabs.com/v1/items/' + id + 
                              '?format=json&apiKey=' + apiKey)
                res_lookup = ur.urlopen(URI_lookup)
                result_lookup = json.loads(res_lookup.read().decode('utf-8'))
                if 'brandName' in result_lookup:
                    b = result_lookup['brandName']
                else:
                    b = 'n/a'

                #if one of the four brands being studied
                if ('Cheerios' in b or 'Kashi' in b or 'Kellogg\'s' in b or 'Post' in b):
                    if 'name' in result['items'][i]:
                        name = result['items'][i]['name']
                    else:
                        name = 'n/a'
                    if 'customerRating' in result_lookup:
                        rating = result['items'][i]['customerRating']
                    else:
                        rating = 0
                    if 'numReviews' in result_lookup:
                        num_review = result['items'][i]['numReviews']
                    else:
                        num_review = 0
                    csvwrite.writerow([b] + [name] + [rating] + [search_num] + [num_review])

    
                    #gather data about brands
                    if 'Cheerios' in b:
                        ch_list[0] += 1
                        if search_num <= 3:
                            ch_list[1] += 1
                    elif 'Kashi' in b:
                        ka_list[0] += 1
                        if search_num <= 3:
                            ka_list[1] += 1
                    elif 'Kellogg\'s' in b:
                        ke_list[0] += 1
                        if search_num <= 3:
                            ke_list[1] += 1
                    elif 'Post' in b:
                        po_list[0] += 1
                        if search_num <= 3:
                            po_list[1] += 1

                search_num += 1
            
            URI = ('http://api.walmartlabs.com/v1/search?start=' + str(start) 
                   + '&numItems=25&query=cereal&format=json&apiKey=' + apiKey)
            response = ur.urlopen(URI)
            html = response.read().decode('utf-8')
            result = json.loads(html)
            start += 25

        #Gather data of "cold cereal" search term
        csvwrite.writerow([' ']*5)
        csvwrite.writerow(['Search Term: Cold Cereal'] + [' ']*4)
        csvwrite.writerow(['Brand'] + ['Cereal Name'] 
                          + ['Rating'] + ['Search Ranking']
                          + ['Num of Reviews']) 
            
        start = 1
        #URI for searching for cold cereal
        URI2 = ('http://api.walmartlabs.com/v1/search?start=' + str(start) 
                + '&numItems=25&query=cold+cereal&format=json&apiKey=' + apiKey)
        response2 = ur.urlopen(URI2)
        html2 = response2.read().decode('utf-8')
        result2 = json.loads(html2)
        
        search_num2 = 1
        totalResults = result2['totalResults']
        start += 25
        while (start <= totalResults and start <= 1000): #pagination limit is top 1000 items

            max = result['numItems']
            for i in range(0,max):
               	#check brand
                id = str(result2['items'][i]['itemId'])
                URI_lookup2 = ('http://api.walmartlabs.com/v1/items/' + id + 
                              '?format=json&apiKey=' + apiKey)
                res_lookup2 = ur.urlopen(URI_lookup2)
                result_lookup2 = json.loads(res_lookup2.read().decode('utf-8'))
                if 'brandName' in result_lookup2:
                    b = result_lookup2['brandName']
                else:
                    b = 'n/a'

                #if one of the four brands being studied
                if ('Cheerios' in b or 'Kashi' in b or 'Kellogg\'s' in b or 'Post' in b):
                    if 'name' in result2['items'][i]:
                        name = result2['items'][i]['name']
                    else:
                        name = 'n/a'
                    if 'customerRating' in result_lookup2:
                        rating = result2['items'][i]['customerRating']
                    else:
                        rating = 0
                    if 'numReviews' in result_lookup2:
                        num_review = result2['items'][i]['numReviews']
                    else:
                        num_review = 0
                    csvwrite.writerow([b] + [name] + [rating] + [search_num2] + [num_review])

    
                    #gather data about brands
                    if 'Cheerios' in b:
                        ch_list[2] += 1
                        if search_num2 <= 3:
                            ch_list[3] += 1
                    elif 'Kashi' in b:
                        ka_list[2] += 1
                        if search_num2 <= 3:
                            ka_list[3] += 1
                    elif 'Kellogg\'s' in b:
                        ke_list[2] += 1
                        if search_num2 <= 3:
                            ke_list[3] += 1
                    elif 'Post' in b:
                        po_list[2] += 1
                        if search_num2 <= 3:
                            po_list[3] += 1

                search_num2 += 1
            
            URI2 = ('http://api.walmartlabs.com/v1/search?start=' + str(start) 
                    + '&numItems=25&query=cold+cereal&format=json&apiKey=' + apiKey)
            response2 = ur.urlopen(URI2)
            html2 = response2.read().decode('utf-8')
            result2 = json.loads(html2)
            start += 25

        #write data about brands to csv file
        csvwrite.writerow([' ']*5)
        csvwrite.writerow(['Brand'] + ['Num of Searches: Cereal'] + ['Top 3: Cereal']
        		  + ['Num of Searches: Cold Cereal'] + ['Top 3: Cold Cereal'])
        csvwrite.writerow(['Cheerios'] + [ch_list[0]] + [ch_list[1]] + [ch_list[2]]
        		  + [ch_list[3]])
        csvwrite.writerow(['Kashi'] + [ka_list[0]] + [ka_list[1]] + [ka_list[2]]
        		  + [ka_list[3]])
        csvwrite.writerow(['Kellogg\'s'] + [ke_list[0]] + [ke_list[1]] + [ke_list[2]]
        		  + [ke_list[3]])
        csvwrite.writerow(['Post'] + [po_list[0]] + [po_list[1]] + [po_list[2]]
        		  + [po_list[3]])
        csvwrite.writerow(['Total num of searches, cereal:'] + [search_num-1]
                          + ['Total num of searches, cold cereal:'] + [search_num2-1] 
                          + [' '])


main()
