#This script is created by Jonathan brahmi


import os

def main():
    logo = ''' 
         [create]    create images to run inside container on docker
                    [and]    Automation for the bofth action  
                             [upload]    upload your images to docker hub\n
    '''
    message = '''
	*Look if the dockerfile already exists its will be give you an error  
        *Attention before you are continue the process edit the dockerfile\n 

    '''
    print(logo)
    print(message)
    file = open(f"dockerfile", "x")
    file.close()
    image_names = str(input("choose and enter images name$"))
    username = str(input("username for login to docker hub to upload the images$"))
    password = str(input("password for login to docker hub to upload the images$"))
    os.system(f"docker build -t {image_names} .")
    os.system(f"docker login --username {username} --password {password}")
    os.system(f"docker push {image_names} ")
    os.system("pause")


main()
