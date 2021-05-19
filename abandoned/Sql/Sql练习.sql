-- 1.查询" 01 "课程比" 02 "课程成绩高的学生的信息及课程分数
SELECT
	a.*,
	b.score AS class1,
	c.score AS class2 
FROM
	Student a
	LEFT JOIN SC b ON a.SId = b.SId 
	AND b.CId = '01'
	LEFT JOIN SC c ON a.SId = c.SId 
	AND
	c.CId = '02' 
WHERE b.score > c.score

SELECT a.*, class1,class2 FROM Student a RIGHT JOIN(
	SELECT t1.SId, class1, class2 FROM
		(SELECT SId, score as class1 FROM sc WHERE CId='01')as t1,
		(SELECT SId, score as class2 FROM sc WHERE CId='02')as t2
	WHERE t1.SId=t2.SId AND class1 > class2
) r ON a.SId=r.SId

-- 1.1查询同时存在" 01 "课程和" 02 "课程的情况
SELECT t1.SId, t1.score FROM 
	(SELECT SId, score, CId FROM sc WHERE CId='01') as t1,
	(SELECT SId, score, CId FROM sc WHERE CId='02') as t2
WHERE t1.SId=t2.SId

SELECT a.*, b.score as class1, c.score as class2 FROM Student a 
	RIGHT JOIN sc b ON a.SId=b.SId AND b.CId='01'
	RIGHT JOIN sc c ON a.SId=c.SId AND c.CId='02'
WHERE a.SId=b.SId

-- 1.2查询存在" 01 "课程但可能不存在" 02 "课程的情况(不存在时显示为 null )
SELECT a.*, b.score as class1, c.score as class2 FROM Student a 
	RIGHT JOIN sc b ON a.SId=b.SId AND b.CId='01'
	LEFT JOIN sc c ON a.SId=c.SId AND c.CId='02'
WHERE a.SId=b.SId

select * from 
	(select * from sc where sc.CId = '01') as t1
	left join 
	(select * from sc where sc.CId = '02') as t2
on t1.SId = t2.SId;

select * from 
	(select * from sc where sc.CId = '02') as t2
	right join 
	(select * from sc where sc.CId = '01') as t1
on t1.SId = t2.SId;

-- 1.3查询不存在" 01 "课程但存在" 02 "课程的情况
SELECT a.*,b.* FROM SC a
	LEFT JOIN Student b ON b.SId=a.SId	
	WHERE a.SId NOT IN(
		SELECT SId FROM SC WHERE SC.CId='01'
	)
AND a.CId='02'

-- 2.查询平均成绩大于等于 60 分的同学的学生编号和学生姓名和平均成绩
SELECT a.* FROM Student a RIGHT JOIN 
(SELECT SId, AVG(score) as avg_score FROM SC  GROUP BY SId HAVING avg_score >= 60) b 
ON a.SId=b.SId
SELECT a.*,avg_score FROM Student a, 
(SELECT SId, AVG(score) as avg_score FROM SC GROUP BY SId HAVING avg_score >= 60) b WHERE a.SId=b.SId  

-- 3.查询在 SC 表存在成绩的学生信息
SELECT DISTINCT a.* FROM Student a RIGHT JOIN SC b ON a.SId=b.SId

SELECT DISTINCT a.* FROM Student a,SC b WHERE a.SId=b.SId

-- 4.查询所有同学的学生编号、学生姓名、选课总数、所有课程的总成绩(没成绩的显示为 null )
SELECT a.*,b.count,b.sum_score FROM Student a LEFT JOIN 
(SELECT SId, COUNT(CId) as count,SUM(score) as sum_score FROM SC GROUP BY SId) b ON a.SId=b.SId

-- 4.1.查有成绩的学生信息
SELECT DISTINCT a.* FROM Student a RIGHT JOIN SC b ON a.SId=b.SId

select * from student
where student.sid in (select sc.sid from sc);

-- 5.查询「李」姓老师的数量
SELECT count(*) as count FROM Teacher WHERE Tname like '李%'

-- 6.查询学过「张三」老师授课的同学的信息
SELECT a.* FROM Student a WHERE a.SId IN 
	(SELECT b.SId FROM SC b RIGHT JOIN Course c ON b.CId=c.CId LEFT JOIN Teacher d ON d.TId=c.TId  WHERE d.Tname='张三')

SELECT a.*,b.score,c.Cname,d.Tname FROM Student a, SC b, Course c, Teacher d
WHERE a.SId=b.SId
AND b.CId=c.CId
AND c.TId=d.TId
AND d.Tname='张三'

-- 7.查询没有学全所有课程的同学的信息
SELECT * FROM Student a WHERE a.SId NOT IN
	(SELECT b.SId FROM Student b RIGHT JOIN SC c ON b.SId=c.SId GROUP BY b.SId HAVING count(b.SId)=(SELECT COUNT(CId) FROM Course))
	
-- 8.查询至少有一门课与学号为" 01 "的同学所学相同的同学的信息
SELECT * FROM Student WHERE Student.SId IN(
SELECT a.SId FROM Student a RIGHT JOIN SC b ON a.SId=b.SId WHERE b.CId IN 
(SELECT CId FROM SC WHERE SId='01')
)

-- 9.查询和" 01 "号的同学学习的课程完全相同的其他同学的信息
SELECT c.*, COUNT(c.SId) as count FROM
	(
		SELECT a.SId, a.Sname FROM Student a LEFT JOIN SC b ON a.SId=b.SId AND b.CId IN (SELECT CId FROM SC WHERE SId='01') 
	) as c
GROUP BY c.Sname HAVING count=(SELECT COUNT(SId) FROM SC WHERE SId='01')

-- 10.查询没学过"张三"老师讲授的任一门课程的学生姓名
SELECT * FROM Student WHERE SId NOT IN (
	SELECT a.SId FROM SC a WHERE a.CId  IN 
	(
		SELECT CId FROM Course c, Teacher t WHERE t.Tname='张三' AND c.TId=t.TId
	)
)

select * from student
    where student.sid not in(
        select sc.sid from sc where sc.cid in(
            select course.cid from course where course.tid in(
                select teacher.tid from teacher where tname = "张三"
            )
        )
    );

-- 11.查询两门及其以上不及格课程的同学的学号，姓名及其平均成绩
SELECT a.*, AVG(s.score) as avg_score, COUNT(a.SId) as count FROM Student a 
	RIGHT JOIN SC s ON a.SId=s.SId AND s.score<=60 
	GROUP BY a.SId HAVING count>=2

select student.sid, student.sname, AVG(sc.score) from student,sc
where 
    student.sid = sc.sid and sc.score<60
group by sc.sid 
having count(*)>1;

-- 12.检索" 01 "课程分数小于 60，按分数降序排列的学生信息
SELECT a.*,b.score as score FROM Student a 
LEFT JOIN SC b ON a.SId=b.SId
WHERE b.score  
AND b.CId='01'  
AND b.score < 60 
ORDER BY b.score DESC

select student.*, sc.score from student, sc
where student.sid = sc.sid
and sc.score < 60
and cid = "01"
ORDER BY sc.score DESC;

-- 13.按平均成绩从高到低显示所有学生的所有课程的成绩以及平均成绩
SELECT a.*, AVG(b.score) as avg_score FROM Student a RIGHT JOIN SC b ON a.SId=b.SId GROUP BY a.SId ORDER BY avg_score DESC

-- 14.查询各科成绩最高分、最低分和平均分：
	-- 以如下形式显示：课程 ID，课程 name，最高分，最低分，平均分，及格率，中等率，优良率，优秀率
	-- 及格为>=60，中等为：70-80，优良为：80-90，优秀为：>=90
	-- 要求输出课程号和选修人数，查询结果按人数降序排列，若人数相同，按课程号升序排列
SELECT SC.CId,COUNT(*) FROM SC WHERE SC.CId='03'
SELECT main.CId,cus.Cname, MAX(main.score) as max, MIN(main.score) as min, AVG(main.score) as avg_score,COUNT(main.CId) as num, pass.pass,general.general,fine.fine,good.good FROM SC main
	LEFT JOIN Course cus ON main.CId=cus.CId
	LEFT JOIN 
		(
			SELECT a.CId,CONCAT(ROUND(a.count/b.count*100,2),'%') as pass FROM
				(SELECT CId, COUNT(*) as count FROM SC WHERE score >= 60 GROUP BY SC.CId) as a 
				LEFT JOIN 
				(SELECT CId, COUNT(*) as count FROM SC GROUP BY SC.CId) as b ON a.CId=b.CId
		) pass
	ON main.CId=pass.CId 
	LEFT JOIN 
	(
		SELECT a.CId,CONCAT(ROUND(a.count/b.count*100,2),'%') as general FROM
			(SELECT CId, COUNT(*) as count FROM SC WHERE score >=70 AND score < 80 GROUP BY SC.CId) as a 
			LEFT JOIN 
			(SELECT CId, COUNT(*) as count FROM SC GROUP BY SC.CId) as b ON a.CId=b.CId
	) as general
	ON main.CId=general.CId 
	LEFT JOIN
	(
		SELECT a.CId,CONCAT(ROUND(a.count/b.count*100,2),'%') as fine FROM
			(SELECT CId, COUNT(*) as count FROM SC WHERE score >=80 and score < 90 GROUP BY SC.CId) as a 
			LEFT JOIN 
			(SELECT CId, COUNT(*) as count FROM SC GROUP BY SC.CId) as b ON a.CId=b.CId
	) as fine
	ON main.CId=fine.CId
	LEFT JOIN
	(
		SELECT a.CId,CONCAT(ROUND(a.count/b.count*100,2),'%') as good FROM
			(SELECT CId, COUNT(*) as count FROM SC WHERE score >= 90 GROUP BY SC.CId) as a 
			LEFT JOIN 
			(SELECT CId, COUNT(*) as count FROM SC GROUP BY SC.CId) as b ON a.CId=b.CId
	) as good
	ON main.CId=good.CId GROUP BY main.CId

-- 14.查询各科成绩最高分、最低分和平均分：
	-- 以如下形式显示：课程 ID，课程 name，最高分，最低分，平均分，及格率，中等率，优良率，优秀率
	-- 及格为>=60，中等为：70-80，优良为：80-90，优秀为：>=90
	-- 要求输出课程号和选修人数，查询结果按人数降序排列，若人数相同，按课程号升序排列
SELECT  
	a.CId as 课程ID,
	b.Cname as '课程 name',
	MAX(a.score) as 最高分数,
	MIN(a.score) as 最低分数,
	AVG(a.score) as 平均分数,
	COUNT(*) as 选修人数,
	CONCAt(SUM(case WHEN a.score >=60 then 1 else 0 end)/COUNT(*)*100,'%') as 及格率,
	CONCAt(SUM(case WHEN a.score >=70 AND a.score < 80  then 1 else 0 end)/COUNT(*)*100,'%') as 中等率,
	CONCAt(SUM(case WHEN a.score >=80 and a.score < 90 then 1 else 0 end)/COUNT(*)*100,'%') as 优良率,
	CONCAt(SUM(case WHEN a.score >=90 then 1 else 0 end)/COUNT(*)*100,'%') as 优秀率
FROM SC a 
LEFT JOIN Course b ON a.CId=b.CId
GROUP BY a.CId ORDER BY '选修人数' DESC,'课程ID' ASC



