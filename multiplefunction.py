class multiple():
    def subfields():
        print("Sub-fields in AI are:")
        lists=['machine learning','neural networks','vision','Robotics','speech processing','Natural language processing']
        for subfieldsAI in lists:
            print(subfieldsAI)
            
    def oddeven():
        num=int(input("Enter a number:"))
        if(num%2==0):
            print(num,"is even number")
            message="is even number"
        else:
            print(num,"is odd number")
            message="is odd number"
        return message
    
    def elegible():
        gender=input("your Gender:")
        age=int(input("your age:"))
        if((age>=21 and gender=="male")or(age>=18 and gender=="female")):
            print("ELIGIBLE")
            marriage="ELIGIBLE"
        else:
            print("NOT ELIGIBLE")
            marriage="NOT ELIGIBLE"
        return marriage
    
    def percentage():
        A=int(input("subject1="))
        B=int(input("subject2="))
        C=int(input("subject3="))
        D=int(input("subject4="))
        E=int(input("subject5="))
        Total=A+B+C+D+E
        percentage=Total/500*100
        print("Total:",Total)
        mark="Total:"
        print("percentage:",percentage)
        mark="percentage:"
        return mark
    
    def triangle():
        Height=int(input("Height:"))
        Breadth=int(input("Breadth:"))
        area=input("area formula:")
        Area=(Height*Breadth)/2
        print("area of Triangle:",Area)
        angle="area of Triangle:"
        Height1=int(input("Height1:"))
        Height2=int(input("Height2:"))
        Breadth=int(input("Breadth:"))
        peri=input("perimeter formula:")
        Peri=Height1+Height2+Breadth
        print("Perimeter of Triangle:",Peri)
        angle="Perimeter of Triangle:"
        return angle
