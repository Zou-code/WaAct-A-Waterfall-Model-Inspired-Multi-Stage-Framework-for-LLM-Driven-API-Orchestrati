from approach.WaAct import WaAct

import os
import sys


current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(current_dir, "approach"))


def run():
    waact = WaAct('tmdb')
    user_requirement = 'Give me the number of movies directed by Sofia Coppola.'
    result = waact.run(user_requirement)
    print(result)
    
if __name__ == '__main__':
    run()