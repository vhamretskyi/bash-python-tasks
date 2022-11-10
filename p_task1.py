
import sys


def get_extension(pytest):
    
    try:
        extension = pytest.split(".")[1]
        print(extension)
    except IndexError:
        print("No extension found")
        raise   
    #except as e:
    #    print(f"Unexpected error: {e}"
    except:
        print("Unexpected error:", sys.exc_info()[0])
    
get_extension("p_task.txt")
