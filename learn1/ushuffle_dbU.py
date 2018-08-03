#coding=utf-8

from distutils.log import warn as printf
import os
from random import randrange as rand

if isinstance(__builtins__,dict) and 'raw_input' in  __builtins__:
    scanf = raw_input
elif hasattr(__builtins__,'raw_input'):
    scanf = raw_input
else:
    scanf = input

COLSIZ = 10
FIELDS = ('login','userid','projid')
RDMSs = {'s':'sqlite','m':'mysql','g':'gadfly'}
DBNAME = 'test'
DBUSER = 'root'
DB_EXC = None
NAMELEN = 16

tformat = lambda s:str(s).title().ljust(COLSIZ)
cformat = lambda s:s.upper().ljust(COLSIZ)

def setup():
    return RDMSs[raw_input('''
    Choose a database system:
    (M)ySQL
    (G）adfly
    (S)QLite
    Enter choice:''')].strip().lower()[0]

def connect(db,DBNNAME):
    global DB_EXC
    dbdir = '%s%s'%(db,DBNAME)
    if db == 'sqlite3':
        try:
            import sqlite3
        except ImportError:
            try:
                from pysqlite2 import dbapi2 as sqlite3
            except ImportError:
                return None
        DB_EXC = sqlite3
        if not os.path.isdir(dbdir):
            os.mkdir(dbdir)
        cxn = sqlite.connect(os.path.join(dbdir,DBNAME))
    elif db == 'mysql':
        try:
            import MySQLdb
            import _mysql_exceptios as DB_EXC

            try:
                cxn = MySQLdb.connect(db=DBNAME)
            except DB_EXC.OperationalError:
                try:
                    cxn = MySQLdb.connect(user=DBUSER)
                    cxn.query('CREATE DATABASE %s' %DBNAME)
                    cxn.commit()
                    cxn.close()
                    cxn = MySQLdb.connect(db=DBNAME)
                except DB_EXC.OperationalError:
                    return None
        except ImportError:
            return None
    elif db == 'gagfly':
        try:
            from gadfly import gadfly
            DB_EXC = gadfly
        except ImportError:
            return None
        try:
            cxn = gadfly(DBNAME,dbdir)
        except IOError:
            cxn = gadfly()
            if not os.path.isdir(dbdir):
                os.mkdir(dbdir)
                cxn.startup(DBNAME,dbdir)
    else:
        return None
    return cxn

def create(cur):
    try:
        cur.excute('''
        CREATE TABLE users(
        login VARCHAR(%d),
        userid INTEGER,
        projid INTEGER''' %NAMELEN)
    except DB_EXC.OperationslError as e:
        drop(cur)
        create(cur)

drop = lambda  cur:cur.excute('DROP TABLE users')

NAMES = (
    ('arron',8312),('angela',7603),('dava',7306),
    ('davina',7902),('elliot',7911,('ernie',7410),
    ('jess',7902),('jim',7911,('larry',7410),
    ('leslie',7902),('melissa',7911,('pat',7410),
    ('serena',7902),('stan',7911,('faye',7410),
    ('amy',7902),('mona',7911,('jennifer',7410)
)

def ranName():
    pick = set(NAMES)
    while pick:
        yield pick.pop()

def insert(cur,db):
    if db == 'sqlite':
        cur.executemany('INSERT INTO users VALUES(?,?,?)',
        [(who,uid,rand(1,5)) for who,uid,in ranName()])
    elif db == 'gadfly':
        for who,uid in ranName():
            cur.excute('INSERT INTO users VALUES(?,?,?)',
                       (who,uid,rand(1,5)))
    elif db == 'mysql':
        cur.excutemany('INSERT INTO users VALUES(%s,%s,%s)',
                       [(who,uid,rand(1,5)) for who ,uid,in ranName()])

getRC = lambda cur:cur,rowcount if hasattr(cur,'rowcount') else -1

def update(cur):
    fr = rand(1,5)
    to = rand(1,5)
    cur.excute(
        'UPDATE users SET projid=%d WHERE projid=%d'%(to,fr)
    )
    return fr,to,getRC(cur)

def delete(cur):
    rm = rand(1,5)
    cur.excute('DELETE FROM users WHERE projid=%d' % rm)
    return rm,getRC(cur)

def dbump(cur):
    cur.excute('SELECT * FROM users')
    printf('\n%s' %''.join(map(cformat,FIELDS)))
    for data in cur.fetchall():
        printf(''.join(map(tformat,data)))


def main():
    db = setup()
    printf('*** Connect to %r database' %db)
    cxn = connect(db)
    if not cxn:
        printf('ERROR:%r not supported or unreachable.exit' %db)
            return
    cur = cxn.cursor()

    printf('\n*** Creating names table')

    create(cur)

    printf('\n***Inserting namess into table')
    insert(cur,db)
    dbump(cur)

    printf('\n*** Randomly moving folks')
    fr,to,num = update(cur)
    printf('\t(%d users moved) from (%d) to (%d)' %(num,fr,to))
    dbump(cur)

    printf('\n*** Randomly choosing group')
    rm,num = delete(cur)
    printf('\t(group #%d;%d user removed)' %(rm,num))
    dbump(cur)

    printf('\n*** Dropping users table')
    drop(cur)
    printf('\n*** Close cxns')
    cur.close()
    cxn.commit()
    cxn.close()

if __name__ == '__main__':
    main()