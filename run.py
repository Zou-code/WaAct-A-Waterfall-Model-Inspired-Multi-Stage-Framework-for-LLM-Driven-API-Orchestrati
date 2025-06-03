from approach.WaAct import WaAct

def run():
    waact = WaAct()
    user_requirement = 'Give me the number of movies directed by Sofia Coppola.'
    result = waact.run(user_requirement)
    print(result)
    
if __name__ == '__main__':
    run()