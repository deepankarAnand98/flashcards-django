from django.shortcuts import render

def home(request):
    return render(request, 'home.html',{})

def add(request):
    from random import randint
    
    num1 = randint(0,11)
    num2 = randint(0,11)

    if request.method == "POST":
        answer = request.POST['answer']
        print(f"\n\n\n{answer}\n\n\n")
        oldnum1 = request.POST['oldnum1'] 
        oldnum2 = request.POST['oldnum2'] 

        if not answer:
            my_answer = "Hey, You Did Not Enter Your Answer"
            color='dark'
            return render(request, 'add.html',{
            'my_answer':my_answer,
            'color':color,
            'num1':num1,
            'num2':num2,
            })

        correct_answer = int(oldnum1) + int(oldnum2)

        if int(answer) == correct_answer:
            my_answer = "Correct! " + oldnum1 + " + " + oldnum2 + " = " + answer 
            color = "primary"
        else:
            my_answer = "Incorrect! " + oldnum1 + " + " + oldnum2 + " is not " + answer +". Correct Answer " + str(correct_answer)
            color = "danger"

        return render(request, 'add.html',{
            'answer':answer,
            'my_answer':my_answer,
            'color':color,
            'num1':num1,
            'num2':num2,
            })
    
    
    return render(request, 'add.html',{
        'num1':num1,
        'num2':num2,
    })

def subtract(request):
    from random import randint
    
    num1 = randint(0,10)
    num2 = randint(0,10)

    print(f"num1: {num1}, num2:{num2}")

    if request.method == "POST":
        answer = request.POST['answer']
        print(f"\n\n\n{answer}\n\n\n")
        oldnum1 = request.POST['oldnum1'] 
        oldnum2 = request.POST['oldnum2']

        if not answer:
            my_answer = "Hey, You Did Not Enter Your Answer"
            color='dark'
            return render(request, 'subtract.html',{
            'my_answer':my_answer,
            'color':color,
            'num1':num1,
            'num2':num2,
            })

        correct_answer = int(oldnum1) - int(oldnum2)

        if int(answer) == correct_answer:
            my_answer = "Correct! " + oldnum1 + " - " + oldnum2 + " = " + answer 
            color = "primary"
        else:
            my_answer = "Incorrect! " + oldnum1 + " - " + oldnum2 + " is not " + answer +". Correct Answer " + str(correct_answer)
            color = "danger"

        return render(request, 'subtract.html',{
            'answer':answer,
            'my_answer':my_answer,
            'color':color,
            'num1':num1,
            'num2':num2,
            })
    
    
    return render(request, 'subtract.html',{
        'num1':num1,
        'num2':num2,
    })

def multiply(request):
    from random import randint
    
    num1 = randint(0,10)
    num2 = randint(0,10)

    print(f"num1: {num1}, num2:{num2}")

    if request.method == "POST":
        answer = request.POST['answer']
        print(f"\n\n\n{answer}\n\n\n")
        oldnum1 = request.POST['oldnum1'] 
        oldnum2 = request.POST['oldnum2'] 

        if not answer:
            my_answer = "Hey, You Did Not Enter Your Answer"
            color='dark'
            return render(request, 'multiply.html',{
            'my_answer':my_answer,
            'color':color,
            'num1':num1,
            'num2':num2,
            })

        correct_answer = int(oldnum1) * int(oldnum2)

        if int(answer) == correct_answer:
            my_answer = "Correct! " + oldnum1 + " - " + oldnum2 + " = " + answer 
            color = "primary"
        else:
            my_answer = "Incorrect! " + oldnum1 + " x " + oldnum2 + " is not " + answer +". Correct Answer " + str(correct_answer)
            color = "danger"

        return render(request, 'multiply.html',{
            'answer':answer,
            'my_answer':my_answer,
            'color':color,
            'num1':num1,
            'num2':num2,
            })
    
    
    return render(request, 'multiply.html',{
        'num1':num1,
        'num2':num2,
    })

def divide(request):
    from random import randint
    
    num1 = randint(0,10)
    num2 = randint(1,10)

    print(f"num1: {num1}, num2:{num2}")

    if request.method == "POST":
        answer = request.POST['answer']
        print(f"\n\n\n{answer}\n\n\n")
        oldnum1 = request.POST['oldnum1'] 
        oldnum2 = request.POST['oldnum2'] 

        if not answer:
            my_answer = "Hey, You Did Not Enter Your Answer"
            color='dark'
            return render(request, 'divide.html',{
            'my_answer':my_answer,
            'color':color,
            'num1':num1,
            'num2':num2,
            })

        correct_answer = round(int(oldnum1) / int(oldnum2),2)

        if float(answer) == correct_answer:
            my_answer = "Correct! " + oldnum1 + " / " + oldnum2 + " = " + answer 
            color = "primary"
        else:
            my_answer = "Incorrect! " + oldnum1 + " / " + oldnum2 + " is not " + answer +". Correct Answer " + str(correct_answer)
            color = "danger"

        return render(request, 'divide.html',{
            'answer':answer,
            'my_answer':my_answer,
            'color':color,
            'num1':num1,
            'num2':num2,
            })
    
    
    return render(request, 'divide.html',{
        'num1':num1,
        'num2':num2,
    })

