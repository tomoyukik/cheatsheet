MATCH (s:Station)-[n:NEXT]->() DELETE n;
MATCH (s:Station) DELETE s;

// CREATE CONSTRAINT ON (station:Station) ASSERT station.number IS UNIQUE;
// 制約のMERGEの方法が知りたい
// MERGE CONSTRAINT ON (station:Station) ASSERT station.number IS UNIQUE;

// 有向グラフなのか？
// 同じリレーションをいくつも定義可能 - 制約作れないか
CREATE (km:Station {number: 'jb23', name: 'kameido'}),
    (kn:Station {number: 'jb22', name: 'kinshicho'}),
    (ry:Station {number: 'jb21', name: 'ryogoku'}),
    (as:Station {number: 'jb20', name: 'asakusabashi'}),
    (ak:Station {number: 'jb19', name: 'akihabara'}),
    (km)-[:NEXT]->(kn),
    (kn)-[:NEXT]->(ry),
    (ry)-[:NEXT]->(as),
    (as)-[:NEXT]->(ak),
    (kn)-[:NEXT]->(km),
    (kn)-[:NEXT]->(km);



