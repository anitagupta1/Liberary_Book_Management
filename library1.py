class lib_rary:
    def __init__(self, libname, lst_of_book):
        self.lbo = lst_of_book
        self.ln = libname
        self.lendb={}

    def display_books(self):
        print("name of books present in library")
        for book, v in self.lbo.items():
            print(book, end="\n")

    def lend_book(self, bookname,prsname):
        if bookname in self.lbo:
            if self.lbo[bookname]==0:
                self.lbo[bookname]=prsname
            else:
                print("lended to "+prsname)
        else:
            print("the book name u enter not present in the libraary")

    def return_book(self,book):
        if book in self.lbo:
           if self.lbo[book]!=0:
              self.lbo[book]=0
           else:
              print(" this book has not lended to anyone\n")
        else:
            print("the book name u enter not present in the libraary")

    def add_book(self,book):
        self.lbo[book]=0

def main():
 booklist={'harry potter & the cursed child':0,'wings of fire':0,'ignited minds':0 , 'beauty and the beast':0,'princess':0,'pinkish':0}
 l=lib_rary('ANITAS LIBERARY' ,booklist)
 print(" WELCOME TO ******************** ANITAS LIBERARY ************************\n ")
 c=1
 while(c):

  print("------------------------------------------------------------------------")
  print("press 1 to display books of library")
  print("press 2 to lend books of library")
  print("press 3 to return books of library")
  print("press 4 to add books of library")
  print("press 5 to take exit from from the library")
  ch=int(input("enter ur choice  : "))
  if ch==1:
       l.display_books()
  elif ch==2:
       bokname=input("enter the book name u want to read  : ")
       personame=input('enter ur name  : ')
       l.lend_book(bokname,personame)
  elif ch==3:
      book=input("enter book name to which u want to lend\n")
      l.return_book(book)
  elif ch==4:
      book=input("enter book name to add in liberary  : 5")
      l.add_book(book)
  elif ch==5:
       c=0

if __name__=="__main__":
    main()