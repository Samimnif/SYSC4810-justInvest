# SYSC4810 Assignment
> [!IMPORTANT]  
> Student Name: Sami Mnif
> ID: 101199669
## Instructions
> run `python3 interface.py` on the VM terminal

## ACL Table
| S/O               | account balance | investment portfolio | contact details of Financial Advisor | contact details of Financial Planner | money market instruments | private consumer instruments |
|-------------------|:---------------:|:--------------------:|:------------------------------------:|:------------------------------------:|:------------------------:|:----------------------------:|
| Client            |        r        |          r           |                  r                   |                                      |                          |                              |
| Premium Client    |        r        |          rw          |                                      |                  r                   |                          |                              |
| Financial Planner |        r        |          rw          |                                      |                                      |            r             |              r               |
| Financial Advisor |        r        |          rw          |                                      |                                      |                          |              r               |
| Teller            |        r        |          r           |                                      |                                      |                          |                              |

## Which Hash Function?

The reason for the usage of SHA-256 is it is one of the most renowned and secure hashing algorithms currently used while
offering less time required to compute a hash.