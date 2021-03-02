struct API
{
   int(*read) (char *raft_uuid[20], char *peer_uuid[20]);
   int(*write) (char *raft_uuid[20], char *peer_uuid[20]);
};

void call_python_func(struct API *my_api);