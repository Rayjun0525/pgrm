# PGRM
PostgreSQL Replication Manager

# 구현을 위한 세부사항

1. 클러스터에서 관리해야한다.
2. 각 postgres 프로세스를 관리해야한다.
3. 2 node에서도 동작해야한다.
4. 각각의 node에서 daemon으로 동작하며 서로 통신해야한다.
5. 