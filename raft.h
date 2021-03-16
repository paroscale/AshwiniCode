//typedef struct API API;
typedef struct 
{     char raft_uuid[20];
      char peer_uuid[20];
   //int (*read) (char *raft_uuid, char* peer_uuid);
   //int (*write) (char *raft_uuid, char* peer_uuid);

}API;

void call_python_func(API *my_api);
void callback_function(int (*fun_ptr)(char *), char *x, char *y);