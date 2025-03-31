def load_data():
    
		#File location to be updated according to your local system file structure.
    with open("/Users/lobsang/Downloads/pythonTsedharProject/Book-Ratings.csv", encoding = 'latin-1') as f:
        ratingList = f.readlines()
        
    with open("/Users/lobsang/Downloads/pythonTsedharProject/Books.csv", encoding = 'latin-1') as f2:
        booksList = f2.readlines()
        b = 0;
        
    user_preference = {}
    
    def isExist(userID, user_pref):
        if userID in user_pref:
            return 1
    
    
    
    for rating in ratingList:
        if b < 1000:
            ratingObj = rating.split(";")
            userID = ratingObj[0]
            isbn = ratingObj[1]
            actualRating = ratingObj[2]
    
            #user Ids, ISBN, book title,authors, year of publication and corresponding rating.
            for book in booksList:
                bookObj = book.split(";")
                bookISBN = bookObj[0]
                title = bookObj[1]
                author = bookObj[2]
                yop = bookObj[3]
                
                if isbn == bookISBN:
                    if isExist(userID, user_preference) == 1:
                        existingList = user_preference.get(userID)
                        newDict = {isbn: [title, author, yop, actualRating]}
                        existingList.insert(0,newDict)
                    else:
                        newDict = {isbn: [title, author, yop, actualRating]}
                        user_preference[userID] = [newDict]
                            
            b = b+1
            
    return user_preference
