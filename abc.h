typedef struct {
	int (*applycb_ptr)(char *raft_uuid, char *peer_uuid);
	int (*readcb_ptr)(char *raft_uuid, char *peer_uuid);
}pmdb_callback_ptr;


void passing_struct_func_ptr( pmdb_callback_ptr *call_back, char *raft_uuid,
								char *peer_uuid);

void c_wrapper_fun(char *raft_uuid, char *peer_uuid, int (*applycb_ptr)(char *, char *),
					int (*readcb_ptr)(char *, char *));

void call_python_func(pmdb_callback_ptr *call_back);