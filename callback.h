typedef struct callbackchar callbackchar;
struct callbackchar
{
  char name[20];
};
void show_somedata(callbackchar somedata);
callbackchar get_somedata(char name[20]);