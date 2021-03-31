struct pmdb_callback_ptr {
	int (*applycb_ptr)(char *raft_uuid, char *peer_uuid);
	int (*readcb_ptr)(char *raft_uuid, char *peer_uuid);
};


void passing_struct_func_ptr(struct pmdb_callback_ptr *call_back, char *raft_uuid,
								char *peer_uuid);

void c_wrapper_fun(char *raft_uuid, char *peer_uuid, int (*applycb_ptr)(char *, char *),
					int (*readcb_ptr)(char *, char *));