#include <fcntl.h>
#include <stdlib.h>
#include <sys/types.h>
#include <dirent.h>
#include <sys/stat.h>
#include <string.h>
#include <stdio.h>
#include <limits.h>
#include <unistd.h>
#include <errno.h>
#include <libgen.h>
#include <sys/shm.h>
#include <sys/wait.h>
#include <pwd.h>

#define BUFFER_SIZE 200
#define RED "\e[0;31m"
#define GRN "\e[0;32m"
#define YEL "\e[0;33m"
#define BLU "\e[0;34m"
#define MAG "\e[0;35m"
#define CYN "\e[0;36m"
#define WHT "\e[0;37m"
#define reset "\e[0m"

char *sciezka(){
    static int first_time=1;
    if(first_time){
        const char* CLEAR_SCRENN_ANSI="\e[1;1H\e[2J";
        write(STDOUT_FILENO,CLEAR_SCRENN_ANSI,12);
        printf(GRN"\n       ~~~~ POWLOKA MICROSHELL ~~~~   \n");
        printf("  ABY ZAKONCZYC DZIALANIE POWLOKI WPISZ: exit\n");
        printf("  ABY WYSWIETLIC WIECEJ INFORMACJI WPISZ: help\n\n" reset); 
        first_time=0;
    }

    char *name,*path; 
    struct passwd *pass; 
    pass=getpwuid(getuid()); 
    name=pass->pw_name;         /*nazwa uzytkownika*/
    
    if( (path=getcwd(NULL, 0)) == NULL)
        perror("nie udalo sie pobrac obecnej sciezki\n");
    else{
        printf("[");
        printf(CYN "%s:",name);
        printf(MAG "%s",path);
        printf(reset"]");
        printf(RED "\n$ " reset);
    }
return path;
}
char *domowykatalog(){
    char *path;
    if( (path=getcwd(NULL, 0)) == NULL)
        perror("nie udalo sie pobrac obecnej sciezki\n");
    return path;
}
char *split(char a[BUFFER_SIZE]){
    char *token = strtok(a," ");
    return token;
}
void help(){
    printf(YEL"~~~~MICROSHELL by Kacper Kalinowski~~~~\n");
    printf("nr studenta: 464966\n\n"reset);
    printf(GRN"Lista komend:\n"reset);
    printf(GRN": help "reset); 
    printf("- Wyswietlenie pomocy programu\n");
    printf(GRN": ls "reset);
    printf("- Wyswietlenie zawartosci folderu\n");
    printf(GRN": cd "reset);
    printf("- Domyslnie przenosi do folderu domowego uzytkownika, z opcja '..' przenosi do folderu nadrzednego, opcja '~' przenosi do folderu domowego, wpisanie sciezki, przenosi do adekwatnej sciezki\n");
    printf(GRN": cp "reset);
    printf("- Kopiuje zawartosc pliku do drugiego pliku\n");
    printf(GRN": mkdir "reset);
    printf("- Stworzenie folderu o danej nazwie\n");
}
void ls(){
    DIR *folder;
    struct dirent *wejscie;
    folder=opendir(".");

    if (folder == NULL)
        perror("Blad funkcji");
    else{
        while ((wejscie = readdir(folder))!=NULL)
            printf("\n %s ", wejscie->d_name);     
        closedir(folder);
    } 
    printf("\n");

}
void cd(char *suffix,char *sciezka,char *domowa){

    char *copy;
    copy = malloc(strlen(sciezka)+1);
    memcpy(copy,sciezka,strlen(sciezka)+1);
    suffix = strtok(NULL," \n");

    if(suffix==NULL)
        chdir(domowa); 
    else if(strcmp(suffix,"..\n")==0){
        char *docelowa;
        int x=strlen(copy);         
        docelowa = malloc(x+1);

        while(copy[x]!='/'){
            x--;
        }
        memcpy(docelowa,copy,x);
        chdir(docelowa);
        }
    else if(strcmp(suffix,"~\n")==0 || strcmp(suffix,"\0")==0 || strcmp(suffix,"\n")==0)
        chdir(domowa);            
    else{
        if(chdir(suffix)==-1)
            perror("Blad przejscia do folderu");
    }
}
void mkd(char *suffix, char *sciezka){
    suffix = strtok(NULL," \n");

    if(mkdir(suffix,0777)==-1)
        perror("Nie udalo sie stworzyc folderu");
    else
        printf("Stworzono folder\n");
}
void copy(char *source){
    int srcFD,destFD,nbread;
    char *buf[BUFFER_SIZE];
    
    source = strtok(NULL," ");
    srcFD = open(source,O_RDONLY);
    if(srcFD==-1)
        perror("Blad otwierania source pliku");
    
    source = strtok(NULL," ");   
    char *dest=source;
    destFD = open(dest,O_WRONLY | O_CREAT | O_TRUNC, S_IRUSR | S_IWUSR | S_IRGRP | S_IWGRP | S_IROTH | S_IWOTH);
    if(destFD==-1)
        perror("Blad otwierania docelowego pliku");

    while((nbread = read(srcFD,buf,BUFFER_SIZE)) > 0){
        if(write(destFD,buf,nbread) != nbread)
            perror("Blad przepisywania pliku");
    }
  
    if(nbread == -1)
        perror("Blad czytania z pliku");
    if(close(srcFD) == -1)
        perror("Blad zamykania pliku source");
    if(close(destFD) == -1)
        perror("Blad zamykania pliku docelowego");
}
void exec(char *komenda){
    char typ[]={' ','\n'};
    char *token = strtok(komenda,typ);
    char *parametr[20]={0};
    int i=0;
    while(token != NULL){
        parametr[i] = token;
        token = strtok(NULL,typ);
        i++;
    }
    parametr[i] = NULL;
    execvp(parametr[0],parametr);
    perror("Blad wykonania execa");
    exit(-1);
}
int main(){
    char *path;
    char *homepath;
    homepath=domowykatalog();
    
    do{
        path=sciezka();
        char in[BUFFER_SIZE];
        fgets(in,BUFFER_SIZE,stdin);
        char linia[BUFFER_SIZE];
        strcpy(linia,in);
        char *komenda = split(in);
        
        while(komenda != NULL){
            if(strcmp(komenda,"exit\n")==0 || strcmp(komenda,"exit")==0)
                return 0;
            else{ 
                if(strcmp(komenda,"help\n")==0 || strcmp(komenda,"help")==0)
                    help();
                else if(strcmp(komenda,"ls\n")==0 || strcmp(komenda,"ls")==0)
                    ls();
                else if(strcmp(komenda,"cd\n")==0 || strcmp(komenda,"cd")==0)
                    cd(komenda,path,homepath);
                else if(strcmp(komenda,"mkdir\n")==0 || strcmp(komenda,"mkdir")==0)
                    mkd(komenda,path);
                else if(strcmp(komenda,"cp\n")==0 || strcmp(komenda,"cp")==0)
                    copy(komenda);
                else if(strcmp(komenda," ")==0 ||strcmp(komenda,"\n")==0)
                    komenda = strtok(NULL," ");
                else {
                    int pid;
                    pid=fork();
                    if(pid==0)
                        exec(linia);
                    else
                        wait(NULL);
                }
            }
            komenda = strtok(NULL," ");
        }
        path=getcwd(NULL,0);

    }while(1);

    free(path);
    free(homepath);
    exit(EXIT_SUCCESS);
return 0;
}