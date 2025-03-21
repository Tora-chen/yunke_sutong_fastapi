-- 这个文件用于初始化数据库。
-- Lecture 表（课程表）
INSERT INTO lecture (id, title, description, uploader_id,cover_path) VALUES
(1, 'CS50 哈佛大学 计算机科学导论 名校公开课【合集·完结】', 'CS50是哈佛大学校内以及 MOOC 平台 edX 上学习人数最多的计算机课程，内容包括：C语言，数据结构、算法，Python (Flask)，前后端网站开发等。', 1,"67042ae5c3a86de9a30d999eeade92f026f0a644.jpg"),
(2, '【浙江大学】Java入门与进阶 翁恺', 'https://mooc.study.163.com/course/ 翁恺老师的精品课之一', 1,"2357c31501ee443aaf61cdcca9567c57.jpg"),
(3, '《高等数学》同济版 2024年更新|宋浩老师', '《高等数学》同济版 宋浩老师 新浪微博：宋浩老师_ice_mouse；下册开始更新新视频了，在专辑的最底部，跟随课堂进度录制。', 2,"db56877bf758e92f813c25705b6d5fc0eed20512.jpg");

-- Video 表（视频表）
INSERT INTO video (id, lecture_id, title, transcript, path) VALUES
(1, 1, '第0周 Scratch 图形编程', '', '/video/11fed637fe754cf69c7a77173972de61.mp4'),

(3, 2, '【零基础】1.1 计算机与编程语言', '', '/video/31fed637fe754cf69c7a77173972de61.mp4'),
(4, 2, '1.2 计算机的思维方式', '',          '/video/41fed637fe754cf69c7a77173972de61.mp4'),
(5, 2, '1.3 准备Java编程软件', '',          '/video/51fed637fe754cf69c7a77173972de61.mp4'),

(6, 3, '1.1 映射', '',          '/video/61fed637fe754cf69c7a77173972de61.mp4'),
(7, 3, '1.1 函数', '',          '/video/71fed637fe754cf69c7a77173972de61.mp4'),
(8, 3, '1.1 函数的几种特性', '', '/video/81fed637fe754cf69c7a77173972de61.mp4');

-- Note 表（笔记表）
INSERT INTO note (video_id, image_path, description, timestamp) VALUES
(1, '/image/c1f8d4fa86174a37b8c563c3c952346b.jpg', '图中人物正在用手比划，字幕显示他在说：“换句话说，我用我的手已经表示了这么多图样了。”这可能涉及手势或手部动作的表达方式。', 300),
(1, '/image/1473cf521b5f424dbac74fcbebfe6bf4.jpg', '当前PPT显示“representation”字样，可能涉及表示法或表示理论的内容。', 600),
(1, '/image/cf5039cb3bc94753b61ffb82956d9e85.jpg', '当前内容正在介绍“抽象”这一概念，屏幕上显示了“abstraction”一词。', 900),
(1, '/image/4274531e5c1d4f43b3bb24b4be0ed57e.jpg', '图中展示了一位演讲者在台上，背景是一幅雕像。字幕显示：“再加上最后一个字节，to form that pixel, and then one more byte,”，可能在讲解图像处理或数据结构相关内容。', 1200),
(1, '/image/f430c94917f749e8a3d41076f9438060.jpg', '当前内容涉及一个数列：2, 4, 6, 8, 10，提示可能是一个不完全的数列。', 1500),
(1, '/image/44b8b76ab5b6433caaac211f9aed1a94.jpg', '当前内容是关于如何简洁准确地表达自己的意图。', 1800),
(1, '/image/853a472d85fa4976af6fcbe83d0e8fca.jpg', '图中展示了一个动画场景，包含一个路灯和垃圾桶。字幕显示“是的，我很喜欢垃圾”，并附有英文翻译。这可能是在讲解与垃圾或环保相关的内容。', 2100),
(1, '/image/a3c17f9579ab4288b59cd263c7209e06.jpg', '图中展示了一个编程界面，左侧是代码块，右侧是舞台。代码块中有一个角色询问名字并等待回答，舞台显示一个角色说“Hello, world”。下方有角色“Snap”的设置选项。', 2400),
(1, '/image/8d21d45df80348e6b7ecdf169a08c082.jpg', 'PPT上显示的是一个软件界面，包含多个窗口和图标。界面中有一个图表，可能用于展示数据或分析结果。整体布局简洁，信息清晰。', 2700),
(1, '/image/dbdf9a1c1ef645499129bbc803d7c496.jpg', '图中展示了一个编程界面，包含“touching”和“mousepos”两个模块，以及“play sound”和“figure”模块。字幕提到“是或否，真或假，1或0的答案”。', 3000),
(1, '/image/f74b1812ed3840b7a3b7fe942c739f5b.jpg', '图中展示了一个编程界面，左侧是代码块，右侧是舞台。代码块包括角色移动、旋转和重复执行等指令，舞台显示一个角色。字幕显示“现在，他依旧走得很快”。', 3300),
(1, '/image/62c9850d06a24788aabac29dea4c8c0f.jpg', '图中展示了一个编程界面，左侧是代码块，右侧是舞台。字幕显示“蓝色人偶有一个很简单的区块”。', 3600),
(1, '/image/d54e7448c95f48ad8d8995ea807bb29b.jpg', '当前内容涉及高级编程语言，如C语言和JavaScript。屏幕上显示的是一个编程环境，可能在讲解代码或编程概念。', 3900),
(1, '/image/957777d4bd714745a40a9293e44f8b85.jpg', 'PPT上展示了多个大学的标志，包括耶鲁、麻省理工、斯坦福、普林斯顿、宾夕法尼亚大学等。旁边有文字提示“Break it down”，可能在分析这些大学的某些特征或排名。', 4200),

(3, '/image/2357c31501ee443aaf61cdcca9567c57.jpg', 'PPT标题为“计算机的语言”，展示了一段十六进制代码。', 300),

(6, '/image/8be75b19ddec4c6b923f86470c5019f5.jpg', '板书内容涉及数学课程，提到“宋浩”和“宋浩老师_ice_mouse”。还提到“站：so...aobigmouse”，以及“微积分”和“概率与数理统计”。', 300),
(6, '/image/4e10955bbe504103b476291e41d82c2a.jpg', '板书内容包括社交媒体账号、B站用户名、书籍名称、学校和机构名称等信息。', 600),
(6, '/image/aeca2c312716436ca5fd415ee6e086bd.jpg', '板书内容涉及社交媒体账号、书籍和教育机构信息，包括微博、B站账号、书籍名称、大学和学院名称等。', 900),
(6, '/image/bb3772ae922048158d79441170e79cdb.jpg', '板书内容涉及数学课程，提到“高等数学”、“线性代数”、“概率统计”等课程。还提到“山大数学”、“中科院”、“英国Queen Mary”等信息，可能与课程背景或教师经历相关。', 1200),
(6, '/image/af2f461c832c4666a4ddf9e28a6f10e1.jpg', '板书内容涉及数学相关主题，包括线性代数、概率统计等。提到了一些社交媒体账号和书籍，如“Song hao big mouse”和“Queen Mary”。还涉及函数、方程和概率等数学概念。', 1500),
(6, '/image/826aae3e1aeb46eb8391820d29367657.jpg', '板书讲解函数的基本概念，包括定义域、值域、映射与函数关系。定义域为X，值域为Y，映射f: X→Y。强调函数的对应关系和元素的约束。', 1800),
(6, '/image/88c6e08a69644cdb8cf26b763656584f.jpg', '板书内容涉及函数映射关系，定义域、值域和对应关系。图中有函数图像和映射示例，强调单射、满射和双射的概念。', 2100),
(6, '/image/1c754621a702480b84ad68edfc2276f1.jpg', '板书内容涉及函数、映射和关系的概念。包括定义域、值域、单射、满射和双射等术语，图示展示了映射关系。', 2400),
(6, '/image/d4f06f58e4064fe891f318cd35769b54.jpg', '板书讲解函数映射的概念，包括单射、满射和复合映射。定义了集合 \(X\)、\(Y\)、\(Z\) 及函数 \(f\)、\(g\)、\(R_f\)。图示展示了映射关系，强调了单射和满射的条件。', 2700);

-- 其他视频的笔记暂时设置为空缺，以测试笔记空缺时的显示


-- Caption 表（存放字幕地址和视频对应信息）
INSERT INTO caption (id, video_id,language,path) VALUES
(1,1,'zh-CN', '/caption/11fed637fe754cf69c7a77173972de61.srt'),
(3,6,'zh-CN', '/caption/61fed637fe754cf69c7a77173972de61.srt');

-- User 表（用户表）
INSERT INTO user (id, username, hashed_password, display_name) VALUES
(1, 'chenzhihu', '$2b$12$VQC03KjwImz0i6BxTWSpAugBd7/DTJZXzcOEhoADlIpuZbPr1CAgm', '陈志虎'),
(2, 'yangjialin', '$2b$12$VQC03KjwImz0i6BxTWSpAugBd7/DTJZXzcOEhoADlIpuZbPr1CAgm', '杨佳林'),
(3, 'video_processor', '$2b$12$VQC03KjwImz0i6BxTWSpAugBd7/DTJZXzcOEhoADlIpuZbPr1CAgm', 'video_processor');

-- Role 表（角色表）
INSERT INTO role (id, name) VALUES
(1, 'ROLE_STUDENT'),
(2, 'ROLE_VIDEO_PROCESSOR');

-- User_Role 表（用户角色表）
INSERT INTO user_role (id, user_id, role_id) VALUES
(1, 1, 1), -- 陈志虎是学生
(2, 2, 1), -- 杨佳林是学生
(3, 3, 2); -- video_processor是视频处理器

-- User_Collection 表（用户收藏表）
INSERT INTO user_collection (id, user_id, lecture_id) VALUES
(1, 1, 1), -- 陈志虎收藏了CS50
(2, 1, 2), -- 陈志虎收藏了Java课程
(3, 2, 1); -- 杨佳林收藏了CS50

-- User_Lecture 表（用户与课程关系表）   *弃用
-- INSERT INTO user_lecture (id, user_id, lecture_id) VALUES
