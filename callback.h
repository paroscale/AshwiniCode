typedef struct callbackchar callbackchar;
struct callbackchar
{
  char s1[20];
  char s2[20];
};
void show_somedata(callbackchar somedata);
callbackchar get_somedata(char s1[20] , char s2[20]);
void library_function(int (*fun_ptr)(char* ,char*), char* x , char* y);