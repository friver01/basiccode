(select distinct name from borrowed, members, books where borrowed.memberNo = members.memberNo 
and borrowed.isbn = books.isbn and category = 'Gardening') 
union (select distinct name from borrowed, members, books where borrowed.memberNo = members.memberNo 
and borrowed.isbn = books.isbn and category = 'Self-Help');