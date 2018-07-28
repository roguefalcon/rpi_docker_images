SET NAMES 'utf8'
SELECT VERSION() AS version
SELECT @@session.sql_mode AS sql_mod
SET SESSION sql_mode='STRICT_TRANS_T
SELECT config_name, config_value
                                FROM phpbb_config
                                WHERE is_dynamic = 1
SELECT u.*, s.*
                                FROM phpbb_sessions s, phpbb_users u
                                WHERE s.session_id = '398f820ec0ede2abfb5cd9271a84f1
                                        AND u.user_id = s.session_user_id
INSERT INTO phpbb_confirm  (confirm_820ec0ede2abfb5cd9271a84f14e', 1, '2VLY', 1340523955)
SELECT lang_iso, lang_local_name
                FROM phpbb_lang
                ORDER BY lang_english_name
SELECT lang_id
                        FROM phpbb_lang
                        WHERE lang_iso = 'en'
SELECT l.*, f.*
                        FROM phpbb_profile_lang l, phpbb_profile_fields f
                        WHERE f.field_active = 1
                                 AND f.field_show_on_reg = 1
                                AND l.lang_id = 1
                                AND l.field_id = f.field_id
                        ORDER BY f.field_order

root@_gateway on phpbb using TCP/IP
SET NAMES 'utf8'
SELECT VERSION() AS version
SELECT @@session.sql_mode AS sql_mod
SET SESSION sql_mode='STRICT_TRANS_T
SELECT config_name, config_value
                                FROM phpbb_config
                                WHERE is_dynamic = 1
SELECT u.*, s.*
                                FROM phpbb_sessions s, phpbb_users u
                                WHERE s.session_id = '398f820ec0ede2abfb5cd9271a84f1
                                        AND u.user_id = s.session_user_id
SELECT code, seed, attempts
                        FROM phpbb_confirm
                        WHERE confirm_id = '139f20b2d4e0b00b1d13fc79ea76cbf6'
                                AND session_id = '398f820ec0ede2abfb5cd9271a84f14e'
                                AND confirm_type = 1

root@_gateway on phpbb using TCP/IP
SET NAMES 'utf8'
SELECT VERSION() AS version
SELECT @@session.sql_mode AS sql_mod
SET SESSION sql_mode='STRICT_TRANS_T
SELECT config_name, config_value
                                FROM phpbb_config
                                WHERE is_dynamic = 1
SELECT u.*, s.*
                                FROM phpbb_sessions s, phpbb_users u
                                WHERE s.session_id = '398f820ec0ede2abfb5cd9271a84f1
                                        AND u.user_id = s.session_user_id
SELECT code, seed, attempts
                        FROM phpbb_confirm
                        WHERE confirm_id = '139f20b2d4e0b00b1d13fc79ea76cbf6'
                                AND session_id = '398f820ec0ede2abfb5cd9271a84f14e'
                                AND confirm_type = 1
SELECT username
                FROM phpbb_users
                WHERE username_clean = 'newuser'
SELECT group_name
                FROM phpbb_groups
                WHERE LOWER(group_name) = 'newuser'
SELECT user_email_hash
                        FROM phpbb_users
                        WHERE user_email_hash = 367080200313
SELECT lang_id
                FROM phpbb_lang
                WHERE lang_iso = 'en'
SELECT lang_id
                        FROM phpbb_lang
                        WHERE lang_iso = 'en'
SELECT l.*, f.*
                        FROM phpbb_profile_lang l, phpbb_profile_fields f
                        WHERE l.lang_id = 1
                                AND f.field_active = 1
                                 AND f.field_show_on_reg = 1
                                AND l.field_id = f.field_id
                        ORDER BY f.field_order
SELECT group_id
                                        FROM phpbb_groups
                                        WHERE group_name = 'REGISTERED'
                                                AND group_type = 3
INSERT INTO phpbb_users  (username, ssions, user_timezone, user_dateformat, user_lang, user_style, user_actkey, user_ip,me, user_lastmark, user_lastvisit, user_lastpost_time, user_lastpage, user_posts, usrivmsg, user_unread_privmsg, user_last_privmsg, user_message_rules, user_full_folderviewonline, user_allow_viewemail, user_allow_massemail, user_sig, user_sig_bbcode_uiFLsQ85FUdz13je5LHUxVBp2fRVEQ3hjiB.g1qIA3EeK8u', 'new@email.com', '367080200313', 2, 12417, 230271, 1, 0, 0, 1532312417, 0, 0, '', 0, '', '', '', 0, 0, 0, 0, 0, 0, -3, 0
INSERT INTO phpbb_user_group  (user_
SELECT group_colour, group_rank, gro
                        FROM phpbb_groups
                        WHERE group_id = 2
UPDATE phpbb_users
                        SET group_id = 2, user_colour = ''
                        WHERE user_id = 49
UPDATE phpbb_forums
                        SET forum_last_poster_colour = ''
                        WHERE forum_last_poster_id = 49
UPDATE phpbb_topics
                        SET topic_first_poster_colour = ''
                        WHERE topic_poster = 49
UPDATE phpbb_topics
                        SET topic_last_poster_colour = ''
                        WHERE topic_last_poster_id = 49
SELECT group_id
                        FROM phpbb_groups
                        WHERE group_name = 'NEWLY_REGISTERED'
                                AND group_type = 3
SELECT user_id, username
                FROM phpbb_users
                WHERE user_id = 49
SELECT user_id, group_leader
                FROM phpbb_user_group
                WHERE user_id = 49
                        AND group_id = 7
SET AUTOCOMMIT=0
INSERT INTO phpbb_user_group  (user_
COMMIT
SET AUTOCOMMIT=1
SELECT *
                        FROM phpbb_acl_roles_data
                        ORDER BY role_id ASC
UPDATE phpbb_users
                        SET user_permissions = '',
                                user_perm_from = 0
                         WHERE user_id = 49
SELECT group_name, group_type
                FROM phpbb_groups
                WHERE group_id = 7
SELECT a.group_id, a.forum_id, a.aut
                        FROM phpbb_acl_groups a, phpbb_acl_options ao
                        WHERE a.auth_role_id = 0
                                AND a.auth_option_id = ao.auth_option_id AND a.group

                                AND ao.auth_option IN ('a_', 'm_')
                        ORDER BY a.forum_id, ao.auth_option
SELECT a.group_id, a.forum_id, r.aut
                        FROM phpbb_acl_groups a, phpbb_acl_roles_data r, phpbb_acl_o
                        WHERE a.auth_role_id = r.role_id
                                AND r.auth_option_id = ao.auth_option_id AND a.group

                                AND ao.auth_option IN ('a_', 'm_')
                        ORDER BY a.forum_id, ao.auth_option
UPDATE phpbb_config
                        SET config_value = '49'
                        WHERE config_name = 'newest_user_id'
UPDATE phpbb_config
                        SET config_value = 'newuser'
                        WHERE config_name = 'newest_username'
UPDATE phpbb_config
                        SET config_value = config_value + 1
                        WHERE config_name = 'num_users'
SELECT group_colour
                        FROM phpbb_groups
                        WHERE group_id = 2
 LIMIT 1
UPDATE phpbb_config
                        SET config_value = ''
                        WHERE config_name = 'newest_user_colour'
SELECT notify
                        FROM phpbb_user_notifications
                        WHERE item_type = 'notification.type.post'
                                AND item_id = 0
                                AND user_id = 49
                                AND method = 'notification.method.email'
INSERT INTO phpbb_user_notificationsotification.method.email', 1)
SELECT notify
                        FROM phpbb_user_notifications
                        WHERE item_type = 'notification.type.topic'
                                AND item_id = 0
                                AND user_id = 49
                                AND method = 'notification.method.email'
INSERT INTO phpbb_user_notificationsnotification.method.email', 1)
DELETE FROM phpbb_confirm
                        WHERE session_id = '398f820ec0ede2abfb5cd9271a84f14e'
                                AND confirm_type = 1
INSERT INTO phpbb_confirm  (confirm_820ec0ede2abfb5cd9271a84f14e', 1, '692HMR', 1577894680)
UPDATE phpbb_sessions SET session_ti
                        WHERE session_id = '398f820ec0ede2abfb5cd9271a84f14e'

root@_gateway on phpbb using TCP/IP
SET NAMES 'utf8'
SELECT VERSION() AS version
SELECT @@session.sql_mode AS sql_mod
SET SESSION sql_mode='STRICT_TRANS_T
SELECT config_name, config_value
                                FROM phpbb_config
                                WHERE is_dynamic = 1
SELECT u.*, s.*
                                FROM phpbb_sessions s, phpbb_users u
                                WHERE s.session_id = 'eb560c0abb2ee1a1748fd56e49423c
                                        AND u.user_id = s.session_user_id
SELECT COUNT(user_id) AS user_count
                FROM phpbb_users
                WHERE user_type = 1
UPDATE phpbb_sessions SET session_ti
                        WHERE session_id = 'eb560c0abb2ee1a1748fd56e49423c32'

root@_gateway on phpbb using TCP/IP
SET NAMES 'utf8'
SELECT VERSION() AS version
SELECT @@session.sql_mode AS sql_mod
SET SESSION sql_mode='STRICT_TRANS_T
SELECT config_name, config_value
                                FROM phpbb_config
                                WHERE is_dynamic = 1
SELECT u.*, s.*
                                FROM phpbb_sessions s, phpbb_users u
                                WHERE s.session_id = 'eb560c0abb2ee1a1748fd56e49423c
                                        AND u.user_id = s.session_user_id
UPDATE phpbb_sessions SET session_ti session_forum_id = 0
                        WHERE session_id = 'eb560c0abb2ee1a1748fd56e49423c32'

root@_gateway on phpbb using TCP/IP
SET NAMES 'utf8'
SELECT VERSION() AS version
SELECT @@session.sql_mode AS sql_mod
SET SESSION sql_mode='STRICT_TRANS_T
SELECT config_name, config_value
                                FROM phpbb_config
                                WHERE is_dynamic = 1
SELECT u.*, s.*
                                FROM phpbb_sessions s, phpbb_users u
                                WHERE s.session_id = 'eb560c0abb2ee1a1748fd56e49423c
                                        AND u.user_id = s.session_user_id
SELECT user_id, username
                FROM phpbb_users
                WHERE username_clean = 'newuser'
SELECT user_id
                                FROM phpbb_users
                                WHERE user_id = '49'
SELECT a.user_id, a.forum_id, a.auth
                        FROM phpbb_acl_users a, phpbb_acl_options ao
                        WHERE a.auth_role_id = 0
                                AND a.auth_option_id = ao.auth_option_id AND a.user_
                                AND a.forum_id = 0
                                AND ao.auth_option LIKE 'u\\_%'
                        ORDER BY a.forum_id, ao.auth_option
SELECT a.user_id, a.forum_id, r.auth
                        FROM phpbb_acl_users a, phpbb_acl_roles_data r, phpbb_acl_op
                        WHERE a.auth_role_id = r.role_id
                                AND r.auth_option_id = ao.auth_option_id AND a.user_
                                AND a.forum_id = 0
                                AND ao.auth_option LIKE 'u\\_%'
                        ORDER BY a.forum_id, ao.auth_option
SELECT user_id as ug_id, username as
                                FROM phpbb_users
                                WHERE user_id = 49
                                ORDER BY username_clean ASC
SELECT *
                        FROM phpbb_acl_roles
                        WHERE role_type = 'u_'
                        ORDER BY role_order ASC
SELECT a.auth_role_id, a.user_id, a.
                        FROM phpbb_acl_users a, phpbb_acl_roles r
                        WHERE a.auth_role_id = r.role_id
                                AND r.role_type = 'u_'
                                AND a.user_id = 49

                        ORDER BY r.role_order ASC
SELECT r.role_id, o.auth_option, r.a
                                FROM phpbb_acl_roles_data r, phpbb_acl_options o
                                WHERE o.auth_option_id = r.auth_option_id
                                        AND r.role_id IN (6, 7, 5, 8, 9, 23)
SELECT group_id, group_name, group_t
                                FROM phpbb_groups
                                ORDER BY group_type DESC, group_name ASC
SELECT ug.*, u.username, u.username_
                FROM phpbb_user_group ug, phpbb_users u
                WHERE ug.user_id = u.user_id
                        AND ug.user_pending = 0 AND  ug.user_id = 49

root@_gateway on phpbb using TCP/IP
SET NAMES 'utf8'
SELECT VERSION() AS version
SELECT @@session.sql_mode AS sql_mod
SET SESSION sql_mode='STRICT_TRANS_T
SELECT config_name, config_value
                                FROM phpbb_config
                                WHERE is_dynamic = 1
SELECT u.*, s.*
                                FROM phpbb_sessions s, phpbb_users u
                                WHERE s.session_id = 'eb560c0abb2ee1a1748fd56e49423c
                                        AND u.user_id = s.session_user_id
SELECT o.auth_option, r.auth_setting
                        FROM phpbb_acl_options o, phpbb_acl_roles_data r
                        WHERE o.auth_option_id = r.auth_option_id
                                AND r.role_id = 6
DELETE FROM phpbb_acl_users
                        WHERE forum_id = 0
                                AND user_id = 49
                                AND auth_option_id IN (91, 92, 94, 100, 117, 122, 93 110, 111, 112, 113, 114, 115, 116, 121)
SELECT role_id
                        FROM phpbb_acl_roles
                        WHERE role_type = 'u_'
DELETE FROM phpbb_acl_users
                                WHERE forum_id = 0
                                        AND user_id = 49
                                        AND auth_option_id = 0
                                        AND auth_role_id IN ('5', '6', '7', '8', '9'
INSERT INTO phpbb_acl_users  (user_i
SELECT *
                        FROM phpbb_acl_roles_data
                        ORDER BY role_id ASC
UPDATE phpbb_users
                        SET user_permissions = '',
                                user_perm_from = 0
SELECT username as name FROM phpbb_u
INSERT INTO phpbb_log  (user_id, log 'LOG_ACL_ADD_USER_GLOBAL_U_', 0, 'a:1:{i:0;s:7:\"newuser\";}')

root@_gateway on phpbb using TCP/IP
SET NAMES 'utf8'
SELECT VERSION() AS version
SELECT @@session.sql_mode AS sql_mod
SET SESSION sql_mode='STRICT_TRANS_T
SELECT config_name, config_value
                                FROM phpbb_config
                                WHERE is_dynamic = 1
SELECT u.*, s.*
                                FROM phpbb_sessions s, phpbb_users u
                                WHERE s.session_id = 'eb560c0abb2ee1a1748fd56e49423c
                                        AND u.user_id = s.session_user_id
SELECT forum_id, auth_option_id, aut
                        FROM phpbb_acl_users
                        WHERE user_id = 2
SELECT a.forum_id, a.auth_option_id,
                        FROM phpbb_acl_groups a, phpbb_user_group ug, phpbb_groups g
                        WHERE a.group_id = ug.group_id
                                AND g.group_id = ug.group_id
                                AND ug.user_pending = 0
                                AND NOT (ug.group_leader = 1 AND g.group_skip_auth =
                                AND ug.user_id = 2
UPDATE phpbb_users
                                SET user_permissions = 'zik0zjzik0zjzik0zg\n\n\nhwby
                                        user_perm_from = 0
                                WHERE user_id = 2

root@_gateway on phpbb using TCP/IP
SET NAMES 'utf8'
SELECT VERSION() AS version
SELECT @@session.sql_mode AS sql_mod
SET SESSION sql_mode='STRICT_TRANS_T
SELECT config_name, config_value
                                FROM phpbb_config
                                WHERE is_dynamic = 1
SELECT u.*, s.*
                                FROM phpbb_sessions s, phpbb_users u
                                WHERE s.session_id = 'eb560c0abb2ee1a1748fd56e49423c
                                        AND u.user_id = s.session_user_id
UPDATE phpbb_sessions SET session_tilocal', session_forum_id = 0
                        WHERE session_id = 'eb560c0abb2ee1a1748fd56e49423c32'

root@_gateway on phpbb using TCP/IP
SET NAMES 'utf8'
SELECT VERSION() AS version
SELECT @@session.sql_mode AS sql_mod
SET SESSION sql_mode='STRICT_TRANS_T
SELECT config_name, config_value
                                FROM phpbb_config
                                WHERE is_dynamic = 1
SELECT u.*, s.*
                                FROM phpbb_sessions s, phpbb_users u
                                WHERE s.session_id = 'eb560c0abb2ee1a1748fd56e49423c
                                        AND u.user_id = s.session_user_id
SELECT user_id, username
                FROM phpbb_users
                WHERE username_clean = 'newuser'
SELECT user_id
                                FROM phpbb_users
                                WHERE user_id = '49'
SELECT forum_id, forum_name, parent_
                FROM phpbb_forums
                ORDER BY left_id ASC

root@_gateway on phpbb using TCP/IP
SET NAMES 'utf8'
SELECT VERSION() AS version
SELECT @@session.sql_mode AS sql_mod
SET SESSION sql_mode='STRICT_TRANS_T
SELECT config_name, config_value
                                FROM phpbb_config
                                WHERE is_dynamic = 1
SELECT u.*, s.*
                                FROM phpbb_sessions s, phpbb_users u
                                WHERE s.session_id = 'eb560c0abb2ee1a1748fd56e49423c
                                        AND u.user_id = s.session_user_id
SELECT forum_id
                                FROM phpbb_forums
                                ORDER BY left_id
SELECT user_id
                                FROM phpbb_users
                                WHERE user_id = 49
SELECT forum_id
                                FROM phpbb_forums
                                WHERE forum_id IN (3, 6, 7, 4, 5)
SELECT a.user_id, a.forum_id, a.auth
                        FROM phpbb_acl_users a, phpbb_acl_options ao
                        WHERE a.auth_role_id = 0
                                AND a.auth_option_id = ao.auth_option_id AND a.user_
                                AND a.forum_id IN (3, 4, 5, 7, 6)
                                AND ao.auth_option LIKE 'f\\_%'
                        ORDER BY a.forum_id, ao.auth_option
SELECT a.user_id, a.forum_id, r.auth
                        FROM phpbb_acl_users a, phpbb_acl_roles_data r, phpbb_acl_op
                        WHERE a.auth_role_id = r.role_id
                                AND r.auth_option_id = ao.auth_option_id AND a.user_
                                AND a.forum_id IN (3, 4, 5, 7, 6)
                                AND ao.auth_option LIKE 'f\\_%'
                        ORDER BY a.forum_id, ao.auth_option
SELECT user_id as ug_id, username as
                                FROM phpbb_users
                                WHERE user_id = 49
                                ORDER BY username_clean ASC
SELECT *
                        FROM phpbb_acl_roles
                        WHERE role_type = 'f_'
                        ORDER BY role_order ASC
SELECT a.auth_role_id, a.user_id, a.
                        FROM phpbb_acl_users a, phpbb_acl_roles r
                        WHERE a.auth_role_id = r.role_id
                                AND r.role_type = 'f_'
                                AND a.user_id = 49

                        ORDER BY r.role_order ASC
SELECT r.role_id, o.auth_option, r.a
                                FROM phpbb_acl_roles_data r, phpbb_acl_options o
                                WHERE o.auth_option_id = r.auth_option_id
                                        AND r.role_id IN (16, 17, 18, 22, 15, 21, 14
SELECT group_id, group_name, group_t
                                FROM phpbb_groups
                                ORDER BY group_type DESC, group_name ASC
SELECT ug.*, u.username, u.username_
                FROM phpbb_user_group ug, phpbb_users u
                WHERE ug.user_id = u.user_id
                        AND ug.user_pending = 0 AND  ug.user_id = 49
