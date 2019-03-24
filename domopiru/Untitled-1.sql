-- SQLite
SELECT M.id as id, M.name, M.status, type, M.created
 FROM minion AS M join
   agent AS A on (M.agent_id = A.id)
 WHERE M.agent_id == 1
 ORDER BY M.name