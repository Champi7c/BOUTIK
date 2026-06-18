-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Hôte : localhost
-- Genere le : Thu. 18 Jun 2026 a 13:39
-- Version du serveur : 10.4.28-MariaDB
-- Version de PHP : 8.0.28

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de données : `boutik`
--

-- --------------------------------------------------------

--

-- --------------------------------------------------------

--
-- Structure de la table `accounts_profile`
--

CREATE TABLE `accounts_profile` (
  `id` bigint(20) NOT NULL,
  `phone` varchar(20) NOT NULL,
  `address` longtext NOT NULL,
  `city` varchar(100) NOT NULL,
  `avatar` varchar(100) DEFAULT NULL,
  `created_at` datetime(6) NOT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Chargement des donnees de la table `accounts_profile`
--

INSERT INTO `accounts_profile` (`id`, `phone`, `address`, `city`, `avatar`, `created_at`, `user_id`) VALUES
(1, '', '', 'Dakar', '', '2026-03-26 01:10:08.071162', 1),
(2, '', '', 'Dakar', '', '2026-03-26 03:42:09.667507', 2),
(3, '', '', 'Dakar', '', '2026-06-06 21:52:34.415199', 3),
(4, '', '', 'Dakar', '', '2026-06-10 23:53:50.916839', 4),
(5, '', '', 'Dakar', '', '2026-06-18 11:55:50.139150', 5);

-- --------------------------------------------------------

--
-- Structure de la table `account_emailaddress`
--

CREATE TABLE `account_emailaddress` (
  `id` int(11) NOT NULL,
  `email` varchar(254) NOT NULL,
  `verified` tinyint(1) NOT NULL,
  `primary` tinyint(1) NOT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Chargement des donnees de la table `account_emailaddress`
--


-- --------------------------------------------------------

--
-- Structure de la table `account_emailconfirmation`
--

CREATE TABLE `account_emailconfirmation` (
  `id` int(11) NOT NULL,
  `created` datetime(6) NOT NULL,
  `sent` datetime(6) DEFAULT NULL,
  `key` varchar(64) NOT NULL,
  `email_address_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Chargement des donnees de la table `account_emailconfirmation`
--


-- --------------------------------------------------------

--
-- Structure de la table `auth_group`
--

CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL,
  `name` varchar(150) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Chargement des donnees de la table `auth_group`
--


-- --------------------------------------------------------

--
-- Structure de la table `auth_group_permissions`
--

CREATE TABLE `auth_group_permissions` (
  `id` bigint(20) NOT NULL,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Chargement des donnees de la table `auth_group_permissions`
--


-- --------------------------------------------------------

--
-- Structure de la table `auth_permission`
--

CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Chargement des donnees de la table `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `content_type_id`, `codename`, `name`) VALUES
(1, 1, 'add_logentry', 'Can add log entry'),
(2, 1, 'change_logentry', 'Can change log entry'),
(3, 1, 'delete_logentry', 'Can delete log entry'),
(4, 1, 'view_logentry', 'Can view log entry'),
(5, 2, 'add_permission', 'Can add permission'),
(6, 2, 'change_permission', 'Can change permission'),
(7, 2, 'delete_permission', 'Can delete permission'),
(8, 2, 'view_permission', 'Can view permission'),
(9, 3, 'add_group', 'Can add group'),
(10, 3, 'change_group', 'Can change group'),
(11, 3, 'delete_group', 'Can delete group'),
(12, 3, 'view_group', 'Can view group'),
(13, 4, 'add_user', 'Can add user'),
(14, 4, 'change_user', 'Can change user'),
(15, 4, 'delete_user', 'Can delete user'),
(16, 4, 'view_user', 'Can view user'),
(17, 5, 'add_contenttype', 'Can add content type'),
(18, 5, 'change_contenttype', 'Can change content type'),
(19, 5, 'delete_contenttype', 'Can delete content type'),
(20, 5, 'view_contenttype', 'Can view content type'),
(21, 6, 'add_session', 'Can add session'),
(22, 6, 'change_session', 'Can change session'),
(23, 6, 'delete_session', 'Can delete session'),
(24, 6, 'view_session', 'Can view session'),
(25, 7, 'add_emailaddress', 'Can add email address'),
(26, 7, 'change_emailaddress', 'Can change email address'),
(27, 7, 'delete_emailaddress', 'Can delete email address'),
(28, 7, 'view_emailaddress', 'Can view email address'),
(29, 8, 'add_emailconfirmation', 'Can add email confirmation'),
(30, 8, 'change_emailconfirmation', 'Can change email confirmation'),
(31, 8, 'delete_emailconfirmation', 'Can delete email confirmation'),
(32, 8, 'view_emailconfirmation', 'Can view email confirmation'),
(33, 9, 'add_socialaccount', 'Can add social account'),
(34, 9, 'change_socialaccount', 'Can change social account'),
(35, 9, 'delete_socialaccount', 'Can delete social account'),
(36, 9, 'view_socialaccount', 'Can view social account'),
(37, 10, 'add_socialapp', 'Can add social application'),
(38, 10, 'change_socialapp', 'Can change social application'),
(39, 10, 'delete_socialapp', 'Can delete social application'),
(40, 10, 'view_socialapp', 'Can view social application'),
(41, 11, 'add_socialtoken', 'Can add social application token'),
(42, 11, 'change_socialtoken', 'Can change social application token'),
(43, 11, 'delete_socialtoken', 'Can delete social application token'),
(44, 11, 'view_socialtoken', 'Can view social application token'),
(45, 12, 'add_banner', 'Can add Bannière'),
(46, 12, 'change_banner', 'Can change Bannière'),
(47, 12, 'delete_banner', 'Can delete Bannière'),
(48, 12, 'view_banner', 'Can view Bannière'),
(49, 13, 'add_category', 'Can add Catégorie'),
(50, 13, 'change_category', 'Can change Catégorie');

INSERT INTO `auth_permission` (`id`, `content_type_id`, `codename`, `name`) VALUES
(51, 13, 'delete_category', 'Can delete Catégorie'),
(52, 13, 'view_category', 'Can view Catégorie'),
(53, 14, 'add_color', 'Can add Couleur'),
(54, 14, 'change_color', 'Can change Couleur'),
(55, 14, 'delete_color', 'Can delete Couleur'),
(56, 14, 'view_color', 'Can view Couleur'),
(57, 15, 'add_size', 'Can add Taille'),
(58, 15, 'change_size', 'Can change Taille'),
(59, 15, 'delete_size', 'Can delete Taille'),
(60, 15, 'view_size', 'Can view Taille'),
(61, 16, 'add_product', 'Can add Produit'),
(62, 16, 'change_product', 'Can change Produit'),
(63, 16, 'delete_product', 'Can delete Produit'),
(64, 16, 'view_product', 'Can view Produit'),
(65, 17, 'add_wishlist', 'Can add Favori'),
(66, 17, 'change_wishlist', 'Can change Favori'),
(67, 17, 'delete_wishlist', 'Can delete Favori'),
(68, 17, 'view_wishlist', 'Can view Favori'),
(69, 18, 'add_productreview', 'Can add Avis'),
(70, 18, 'change_productreview', 'Can change Avis'),
(71, 18, 'delete_productreview', 'Can delete Avis'),
(72, 18, 'view_productreview', 'Can view Avis'),
(73, 19, 'add_cart', 'Can add Panier'),
(74, 19, 'change_cart', 'Can change Panier'),
(75, 19, 'delete_cart', 'Can delete Panier'),
(76, 19, 'view_cart', 'Can view Panier'),
(77, 20, 'add_orderitem', 'Can add Article'),
(78, 20, 'change_orderitem', 'Can change Article'),
(79, 20, 'delete_orderitem', 'Can delete Article'),
(80, 20, 'view_orderitem', 'Can view Article'),
(81, 21, 'add_order', 'Can add Commande'),
(82, 21, 'change_order', 'Can change Commande'),
(83, 21, 'delete_order', 'Can delete Commande'),
(84, 21, 'view_order', 'Can view Commande'),
(85, 22, 'add_cartitem', 'Can add Article panier'),
(86, 22, 'change_cartitem', 'Can change Article panier'),
(87, 22, 'delete_cartitem', 'Can delete Article panier'),
(88, 22, 'view_cartitem', 'Can view Article panier'),
(89, 23, 'add_profile', 'Can add Profil'),
(90, 23, 'change_profile', 'Can change Profil'),
(91, 23, 'delete_profile', 'Can delete Profil'),
(92, 23, 'view_profile', 'Can view Profil'),
(93, 24, 'add_payment', 'Can add Paiement'),
(94, 24, 'change_payment', 'Can change Paiement'),
(95, 24, 'delete_payment', 'Can delete Paiement'),
(96, 24, 'view_payment', 'Can view Paiement'),
(97, 25, 'add_site', 'Can add site'),
(98, 25, 'change_site', 'Can change site'),
(99, 25, 'delete_site', 'Can delete site'),
(100, 25, 'view_site', 'Can view site');

-- --------------------------------------------------------

--
-- Structure de la table `auth_user`
--

CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Chargement des donnees de la table `auth_user`
--

INSERT INTO `auth_user` (`id`, `password`, `last_login`, `is_superuser`, `username`, `last_name`, `email`, `is_staff`, `is_active`, `date_joined`, `first_name`) VALUES
(1, 'pbkdf2_sha256$600000$tBgFHov9dMY7uO7TvMXuk5$e+LtXBNGmvntJm/KLPrx24fHzwcZvf/YPBUQlD/NZNg=', '2026-06-07 20:10:53.402569', 1, 'admin', '', 'thiambusiness44@gmail.com', 1, 1, '2026-03-26 01:10:07.771112', ''),
(2, 'pbkdf2_sha256$600000$cI3rpRGoEZiWGzaOKAZpGX$TY8yfK7FZhT/4ivItKFPyHA9cKPHwY+nmD8uOMxdpmQ=', '2026-03-26 03:42:33.337616', 0, 'omzi', '', '', 0, 1, '2026-03-26 03:42:09.438282', ''),
(3, 'pbkdf2_sha256$600000$6HOukyN8vfplZxm6aSAXg2$i5ieJ1CI++o278cvE8l99uYk3Lbzetmpala1CxaoDhs=', '2026-06-06 22:21:04.741696', 1, 'administrateur', '', 'a@gmail.com', 1, 1, '2026-06-06 21:52:34.286986', ''),
(4, 'pbkdf2_sha256$600000$EjOOPhJEe5kuxJhLJUyjRk$8wVffDUEbxc1IvZk9at+We8ORyN513e13dp7MFZba60=', '2026-06-10 23:53:51.000547', 0, 'bosse', 'ndoye', 'Bossendoye0@gmail.com', 0, 1, '2026-06-10 23:53:50.458161', 'momar'),
(5, 'pbkdf2_sha256$600000$hkfiWIGNFEZK55xbyhXJwk$PNLJpnYJJn+4/6Ae+A415IEenTYVT8EA1mgjkAuxLjI=', '2026-06-18 11:56:18.335980', 1, 'momar', '', 'mo@gmail.com', 1, 1, '2026-06-18 11:55:49.771128', '');

-- --------------------------------------------------------

--
-- Structure de la table `auth_user_groups`
--

CREATE TABLE `auth_user_groups` (
  `id` bigint(20) NOT NULL,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Chargement des donnees de la table `auth_user_groups`
--


-- --------------------------------------------------------

--
-- Structure de la table `auth_user_user_permissions`
--

CREATE TABLE `auth_user_user_permissions` (
  `id` bigint(20) NOT NULL,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Chargement des donnees de la table `auth_user_user_permissions`
--


-- --------------------------------------------------------

--
-- Structure de la table `django_admin_log`
--

CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext DEFAULT NULL,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) UNSIGNED NOT NULL CHECK (`action_flag` >= 0),
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Chargement des donnees de la table `django_admin_log`
--

INSERT INTO `django_admin_log` (`id`, `object_id`, `object_repr`, `action_flag`, `change_message`, `content_type_id`, `user_id`, `action_time`) VALUES
(1, '68', 'JEAN FLARED', 2, '[{\\"changed\\": {\\"fields\\": [\\"Nom\\"]}}]', 16, 1, '2026-03-26 03:41:21.161701'),
(2, '2', 'omzi', 1, '[{\\"added\\": {}}]', 4, 1, '2026-03-26 03:42:09.670438'),
(3, '98', 'hoodie', 1, '[{\\"added\\": {}}]', 16, 3, '2026-06-06 21:57:08.833113'),
(4, '98', 'hoodie', 3, '', 16, 3, '2026-06-06 22:29:54.300459');

-- --------------------------------------------------------

--
-- Structure de la table `django_content_type`
--

CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Chargement des donnees de la table `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(1, 'admin', 'logentry'),
(2, 'auth', 'permission'),
(3, 'auth', 'group'),
(4, 'auth', 'user'),
(5, 'contenttypes', 'contenttype'),
(6, 'sessions', 'session'),
(7, 'account', 'emailaddress'),
(8, 'account', 'emailconfirmation'),
(9, 'socialaccount', 'socialaccount'),
(10, 'socialaccount', 'socialapp'),
(11, 'socialaccount', 'socialtoken'),
(12, 'store', 'banner'),
(13, 'store', 'category'),
(14, 'store', 'color'),
(15, 'store', 'size'),
(16, 'store', 'product'),
(17, 'store', 'wishlist'),
(18, 'store', 'productreview'),
(19, 'orders', 'cart'),
(20, 'orders', 'orderitem'),
(21, 'orders', 'order'),
(22, 'orders', 'cartitem'),
(23, 'accounts', 'profile'),
(24, 'payments', 'payment'),
(25, 'sites', 'site');

-- --------------------------------------------------------

--
-- Structure de la table `django_migrations`
--

CREATE TABLE `django_migrations` (
  `id` bigint(20) NOT NULL,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Chargement des donnees de la table `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2026-06-10 23:03:10.097821'),
(2, 'auth', '0001_initial', '2026-06-10 23:03:10.124972'),
(3, 'account', '0001_initial', '2026-06-10 23:03:10.154037'),
(4, 'account', '0002_email_max_length', '2026-06-10 23:03:10.175585'),
(5, 'account', '0003_alter_emailaddress_create_unique_verified_email', '2026-06-10 23:03:10.197495'),
(6, 'account', '0004_alter_emailaddress_drop_unique_email', '2026-06-10 23:03:10.299793'),
(7, 'account', '0005_emailaddress_idx_upper_email', '2026-06-10 23:03:10.319699'),
(8, 'account', '0006_emailaddress_lower', '2026-06-10 23:03:10.335861'),
(9, 'account', '0007_emailaddress_idx_email', '2026-06-10 23:03:10.361307'),
(10, 'account', '0008_emailaddress_unique_primary_email_fixup', '2026-06-10 23:03:10.378552'),
(11, 'account', '0009_emailaddress_unique_primary_email', '2026-06-10 23:03:10.392786'),
(12, 'accounts', '0001_initial', '2026-06-10 23:03:10.407247'),
(13, 'admin', '0001_initial', '2026-06-10 23:03:10.427216'),
(14, 'admin', '0002_logentry_remove_auto_add', '2026-06-10 23:03:10.466583'),
(15, 'admin', '0003_logentry_add_action_flag_choices', '2026-06-10 23:03:10.485676'),
(16, 'contenttypes', '0002_remove_content_type_name', '2026-06-10 23:03:10.513265'),
(17, 'auth', '0002_alter_permission_name_max_length', '2026-06-10 23:03:10.531848'),
(18, 'auth', '0003_alter_user_email_max_length', '2026-06-10 23:03:10.552265'),
(19, 'auth', '0004_alter_user_username_opts', '2026-06-10 23:03:10.568766'),
(20, 'auth', '0005_alter_user_last_login_null', '2026-06-10 23:03:10.587176'),
(21, 'auth', '0006_require_contenttypes_0002', '2026-06-10 23:03:10.595758'),
(22, 'auth', '0007_alter_validators_add_error_messages', '2026-06-10 23:03:10.614753'),
(23, 'auth', '0008_alter_user_username_max_length', '2026-06-10 23:03:10.635660'),
(24, 'auth', '0009_alter_user_last_name_max_length', '2026-06-10 23:03:10.653290'),
(25, 'auth', '0010_alter_group_name_max_length', '2026-06-10 23:03:10.670390'),
(26, 'auth', '0011_update_proxy_permissions', '2026-06-10 23:03:10.683077'),
(27, 'auth', '0012_alter_user_first_name_max_length', '2026-06-10 23:03:10.746084'),
(28, 'store', '0001_initial', '2026-06-10 23:03:10.904693'),
(29, 'orders', '0001_initial', '2026-06-10 23:03:10.972319'),
(30, 'payments', '0001_initial', '2026-06-10 23:03:10.999827'),
(31, 'sessions', '0001_initial', '2026-06-10 23:03:11.024368'),
(32, 'socialaccount', '0001_initial', '2026-06-10 23:03:11.093704'),
(33, 'socialaccount', '0002_token_max_lengths', '2026-06-10 23:03:11.146477'),
(34, 'socialaccount', '0003_extra_data_default_dict', '2026-06-10 23:03:11.161877'),
(35, 'socialaccount', '0004_app_provider_id_settings', '2026-06-10 23:03:11.196688'),
(36, 'socialaccount', '0005_socialtoken_nullable_app', '2026-06-10 23:03:11.367489'),
(37, 'socialaccount', '0006_alter_socialaccount_extra_data', '2026-06-10 23:03:11.390048'),
(38, 'sites', '0001_initial', '2026-06-18 11:52:25.161886'),
(39, 'sites', '0002_alter_domain_unique', '2026-06-18 11:52:25.161886'),
(40, 'orders', '0002_alter_order_payment_method', '2026-06-18 11:52:46.798007'),
(41, 'payments', '0002_alter_payment_provider', '2026-06-18 11:52:46.812254');

-- --------------------------------------------------------

--
-- Structure de la table `django_session`
--

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Chargement des donnees de la table `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('n5w823bc4bn9n19qtkpidzsxkgd75c3n', '.eJw1jrsOwjAMRX8FRWLrw01FK7oxsrAwsCBFpo1KoE1DHgNU_XccUeTB9j1X155Zi9azZmb7WojYjZ260HqhOtaQyBL2Cqi98m_WFAlh1UoifAcABJ36xJWmdhom-xs1jlE8a4lPad3mdA0AN-AlMTViH2E-yk5hvp5zuVvNgpfickfvDsZsORyjnTpVlUKZ8ooW9FHhGa-zgmcPI_v4yRB6yv3npJrOLcvyBVMdREY:1wXSFE:ZAdNjLeN3l4rzFW0Vn39WLWpeXAw2AoWg2Fjr4Vs6ug', '2026-06-24 23:22:00.826022'),
('91l4mt0mkgmyjvjjlg29nr8amh16b1qs', '.eJw1jrsOwjAMRX8FRWLrw01FK7oxsrAwsCBFpo1KoE1DHgNU_XccUeTB9j1X155Zi9azZmb7WojYjZ260HqhOtaQyBL2Cqi98m_WFAlh1UoifAcABJ36xJWmdhom-xs1jlE8a4lPad3mdA0AN-AlMTViH2E-yk5hvp5zuVvNgpfickfvDsZsORyjnTpVlUKZ8ooW9FHhGa-zgmcPI_v4yRB6yv3npJrOLcvyBVMdREY:1wXSGD:9LuJQuP0nK8qxfBb5e8QzSvXQQMCn4fZUj4-0ygN_Ic', '2026-06-24 23:23:01.063880'),
('61hcbtmz7n7bm2hxuz91m1m6f6ot22nk', 'eyJjYXJ0Ijp7fX0:1wXSGt:8n61zY4uHjdtanw-BCs7iTZMTkeHo40AGRUo2OJ9zkA', '2026-06-24 23:23:43.126122'),
('dzzivyu853stqayipub85g4ejp4nckp5', 'eyJjYXJ0Ijp7fX0:1wXSML:FDYReDIEeL7Up1UJDvS3-p0gFKvKK8tR9zc7sjOeiqc', '2026-06-24 23:29:21.033185'),
('29wdbc0366v9asoour6t4zo9v4debluu', 'eyJjYXJ0Ijp7fX0:1wXSMl:ZyuUlWeGiX809-sY8sArRkiVP04I17FD_QLtkk-XBhs', '2026-06-24 23:29:47.193273'),
('238swpzuqli83x1bd5w05ait3jm6mwsg', 'eyJjYXJ0Ijp7fX0:1wXSPx:llzglNE3CjsVxpNR4PjOvBUzFtVB4JGHoaSp8FMbH04', '2026-06-24 23:33:05.299931'),
('oyhr6npo7o9lolbkjcbj2vm1n0a6ruo2', '.eJxVjj9vwyAQxb9KhdQtIUAC_rO1W4d26dClEjrgapM42DV4aKN894LiSq0Yjnu_d-_uQjQsqddLxFl7R1oiyeavZsCeMBTgjhC6kdoxpNkbWix0pZE-jw6Hx9X7L6CH2OfpGjlWtXXGAOOAsqoqzhxKZeAgjGqwASkkr1EgHCxDXn1YC3uunAOoAXOohTmR9kIapXWp0zy6xabb2Y3Kjs8FQvLpi7R8k7G3mImQjLEMo_8ubQkah3G-fQOci_gaEE44x7uX94Uxw4TIzJ-hK3B3Rudht66Lu7iatRD6rYcUH6bpXrCnYs81P7Vl-61QuYFUFEFFRVlDjxN25ZJh6XLub8425HXX6_UHzHV8jQ:1waBYw:LEyDKe1A3FDlTx0YSWmGRyxlRnuJ-0mZEcTOg2fdgMM', '2026-07-02 12:09:38.975736');

-- --------------------------------------------------------

--
-- Structure de la table `orders_cart`
--

CREATE TABLE `orders_cart` (
  `id` bigint(20) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Chargement des donnees de la table `orders_cart`
--


-- --------------------------------------------------------

--
-- Structure de la table `orders_cartitem`
--

CREATE TABLE `orders_cartitem` (
  `id` bigint(20) NOT NULL,
  `quantity` int(11) NOT NULL,
  `cart_id` bigint(20) NOT NULL,
  `color_id` bigint(20) DEFAULT NULL,
  `product_id` bigint(20) NOT NULL,
  `size_id` bigint(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Chargement des donnees de la table `orders_cartitem`
--


-- --------------------------------------------------------

--
-- Structure de la table `orders_order`
--

CREATE TABLE `orders_order` (
  `id` bigint(20) NOT NULL,
  `total` decimal(10,0) NOT NULL,
  `status` varchar(20) NOT NULL,
  `delivery_type` varchar(20) NOT NULL,
  `delivery_address` longtext NOT NULL,
  `delivery_fee` decimal(6,0) NOT NULL,
  `phone` varchar(20) NOT NULL,
  `payment_method` varchar(20) NOT NULL,
  `payment_status` varchar(20) NOT NULL,
  `order_number` varchar(20) NOT NULL,
  `notes` longtext NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Chargement des donnees de la table `orders_order`
--

INSERT INTO `orders_order` (`id`, `total`, `status`, `delivery_type`, `delivery_address`, `delivery_fee`, `phone`, `payment_method`, `payment_status`, `order_number`, `notes`, `created_at`, `updated_at`, `user_id`) VALUES
(1, 25000, 'pending', 'livraison', '', 1500, '781576224', 'stripe', 'pending', 'TS171264', '', '2026-06-10 23:54:33.494379', '2026-06-10 23:54:33.576972', 4);

-- --------------------------------------------------------

--
-- Structure de la table `orders_orderitem`
--

CREATE TABLE `orders_orderitem` (
  `id` bigint(20) NOT NULL,
  `quantity` int(11) NOT NULL,
  `unit_price` decimal(10,0) NOT NULL,
  `color_id` bigint(20) DEFAULT NULL,
  `product_id` bigint(20) NOT NULL,
  `size_id` bigint(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Chargement des donnees de la table `orders_orderitem`
--

INSERT INTO `orders_orderitem` (`id`, `quantity`, `unit_price`, `color_id`, `product_id`, `size_id`) VALUES
(1, 1, 25000, NULL, 92, NULL);

-- --------------------------------------------------------

--
-- Structure de la table `orders_order_items`
--

CREATE TABLE `orders_order_items` (
  `id` bigint(20) NOT NULL,
  `order_id` bigint(20) NOT NULL,
  `orderitem_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Chargement des donnees de la table `orders_order_items`
--

INSERT INTO `orders_order_items` (`id`, `order_id`, `orderitem_id`) VALUES
(1, 1, 1);

-- --------------------------------------------------------

--
-- Structure de la table `payments_payment`
--

CREATE TABLE `payments_payment` (
  `id` bigint(20) NOT NULL,
  `provider` varchar(20) NOT NULL,
  `amount` decimal(10,0) NOT NULL,
  `status` varchar(20) NOT NULL,
  `transaction_id` varchar(200) NOT NULL,
  `reference` varchar(200) NOT NULL,
  `phone_number` varchar(20) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `order_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Chargement des donnees de la table `payments_payment`
--


-- --------------------------------------------------------

--
-- Structure de la table `socialaccount_socialaccount`
--

CREATE TABLE `socialaccount_socialaccount` (
  `id` int(11) NOT NULL,
  `provider` varchar(200) NOT NULL,
  `uid` varchar(191) NOT NULL,
  `last_login` datetime(6) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  `extra_data` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NOT NULL CHECK (json_valid(`extra_data`)),
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Chargement des donnees de la table `socialaccount_socialaccount`
--


-- --------------------------------------------------------

--
-- Structure de la table `socialaccount_socialapp`
--

CREATE TABLE `socialaccount_socialapp` (
  `id` int(11) NOT NULL,
  `provider` varchar(30) NOT NULL,
  `name` varchar(40) NOT NULL,
  `client_id` varchar(191) NOT NULL,
  `secret` varchar(191) NOT NULL,
  `key` varchar(191) NOT NULL,
  `provider_id` varchar(200) NOT NULL,
  `settings` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NOT NULL CHECK (json_valid(`settings`))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Chargement des donnees de la table `socialaccount_socialapp`
--


-- --------------------------------------------------------

--
-- Structure de la table `socialaccount_socialtoken`
--

CREATE TABLE `socialaccount_socialtoken` (
  `id` int(11) NOT NULL,
  `token` longtext NOT NULL,
  `token_secret` longtext NOT NULL,
  `expires_at` datetime(6) DEFAULT NULL,
  `account_id` int(11) NOT NULL,
  `app_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Chargement des donnees de la table `socialaccount_socialtoken`
--


-- --------------------------------------------------------

--
-- Structure de la table `store_banner`
--

CREATE TABLE `store_banner` (
  `id` bigint(20) NOT NULL,
  `title` varchar(200) NOT NULL,
  `subtitle` varchar(300) NOT NULL,
  `image` varchar(100) NOT NULL,
  `link` varchar(200) NOT NULL,
  `button_text` varchar(50) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `order` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Chargement des donnees de la table `store_banner`
--


-- --------------------------------------------------------

--
-- Structure de la table `store_category`
--

CREATE TABLE `store_category` (
  `id` bigint(20) NOT NULL,
  `name` varchar(100) NOT NULL,
  `slug` varchar(50) NOT NULL,
  `image` varchar(100) DEFAULT NULL,
  `description` longtext NOT NULL,
  `order` int(11) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `parent_id` bigint(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Chargement des donnees de la table `store_category`
--

INSERT INTO `store_category` (`id`, `name`, `slug`, `image`, `description`, `order`, `is_active`, `parent_id`) VALUES
(1, 'Chaussures', 'chaussures', 'categories/chaussures.jpg', '', 1, 1, NULL),
(2, 'Vêtements Homme', 'vetements-homme', 'categories/homme.jpg', '', 2, 1, NULL),
(4, 'Accessoires', 'accessoires', 'categories/accessoires.jpg', '', 4, 1, NULL),
(7, 'Sneakers', 'sneakers', '', '', 1, 1, 1),
(8, 'Baskets', 'baskets', '', '', 2, 1, 1),
(9, 'Boots', 'boots', '', '', 3, 1, 1),
(10, 'Sandales', 'sandales', '', '', 4, 1, 1),
(11, 'T-shirts Homme', 't-shirts-homme', '', '', 1, 1, 2),
(12, 'Hoodies', 'hoodies', '', '', 2, 1, 2),
(13, 'Pantalons', 'pantalons', '', '', 3, 1, 2),
(14, 'Vestes Homme', 'vestes-homme', '', '', 4, 1, 2),
(15, 'Shorts', 'shorts', '', '', 5, 1, 2),
(20, 'Casquettes', 'casquettes', '', '', 1, 1, 4),
(21, 'Sacs', 'sacs', '', '', 2, 1, 4),
(22, 'Ceintures', 'ceintures', '', '', 3, 1, 4),
(23, 'Chaussettes', 'chaussettes', '', '', 4, 1, 4);

-- --------------------------------------------------------

--
-- Structure de la table `store_color`
--

CREATE TABLE `store_color` (
  `id` bigint(20) NOT NULL,
  `name` varchar(50) NOT NULL,
  `hex_code` varchar(7) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Chargement des donnees de la table `store_color`
--

INSERT INTO `store_color` (`id`, `name`, `hex_code`) VALUES
(1, 'Noir', '#000000'),
(2, 'Blanc', '#FFFFFF'),
(3, 'Gris', '#808080'),
(4, 'Rouge', '#FF0000'),
(5, 'Bleu', '#0000FF'),
(6, 'Bleu Marine', '#001F5B'),
(7, 'Vert', '#008000'),
(8, 'Kaki', '#8B7355'),
(9, 'Beige', '#F5DEB3'),
(10, 'Marron', '#8B4513'),
(11, 'Orange', '#FFA500'),
(12, 'Jaune', '#FFD700'),
(13, 'Rose', '#FF69B4'),
(14, 'Violet', '#800080'),
(15, 'Bordeaux', '#800020');

-- --------------------------------------------------------

--
-- Structure de la table `store_product`
--

CREATE TABLE `store_product` (
  `id` bigint(20) NOT NULL,
  `name` varchar(200) NOT NULL,
  `slug` varchar(250) NOT NULL,
  `description` longtext NOT NULL,
  `price` decimal(10,0) NOT NULL,
  `discount_price` decimal(10,0) DEFAULT NULL,
  `stock` int(11) NOT NULL,
  `image` varchar(100) NOT NULL,
  `image2` varchar(100) DEFAULT NULL,
  `image3` varchar(100) DEFAULT NULL,
  `is_featured` tinyint(1) NOT NULL,
  `is_new` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `views_count` int(11) NOT NULL,
  `sales_count` int(11) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `category_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Chargement des donnees de la table `store_product`
--

INSERT INTO `store_product` (`id`, `name`, `slug`, `description`, `price`, `discount_price`, `stock`, `image`, `image2`, `image3`, `is_featured`, `is_new`, `is_active`, `views_count`, `sales_count`, `created_at`, `updated_at`, `category_id`) VALUES
(1, 'Urban Street Tee Noir', 'urban-street-tee-noir', 'T-shirt streetwear coupe urbaine, parfait pour un look casual au quotidien.', 7500, NULL, 25, 'products/shirt1.jpg', '', '', 1, 1, 1, 0, 0, '2026-03-26 02:06:27.306215', '2026-03-26 02:06:27.306410', 11),
(2, 'Downtown Graphic Tee', 'downtown-graphic-tee', 'T-shirt graphique avec imprimé downtown. Matière douce et confortable.', 8500, 6500, 25, 'products/shirt2.jpg', '', '', 0, 1, 1, 0, 0, '2026-03-26 02:06:27.328244', '2026-03-26 02:06:27.328263', 11),
(3, 'OG Classic White Tee', 'og-classic-white-tee', 'Le classique blanc indémodable. Coupe clean et minimaliste.', 6500, NULL, 25, 'products/shirt3.jpg', '', '', 1, 0, 1, 0, 0, '2026-03-26 02:06:27.338908', '2026-03-26 02:06:27.338921', 11),
(4, 'Oversize Drop Shoulder Tee', 'oversize-drop-shoulder-tee', 'Coupe oversize drop shoulder tendance. Idéal pour un style relaxed.', 9500, NULL, 25, 'products/shirt4.jpg', '', '', 1, 1, 1, 0, 0, '2026-03-26 02:06:27.345744', '2026-03-26 02:06:27.345758', 11),
(5, 'Boxy Fit Essential Tee', 'boxy-fit-essential-tee', 'Coupe boxy fit essentiel, polyvalent et confortable pour toutes occasions.', 7000, 5500, 25, 'products/shirt5.jpg', '', '', 0, 0, 1, 0, 0, '2026-03-26 02:06:27.353934', '2026-03-26 02:06:27.353946', 11),
(6, 'Street Culture Graphic Tee', 'street-culture-graphic-tee', 'T-shirt graphique street culture avec artwork exclusif ThiamStreetwear.', 8000, NULL, 25, 'products/shirt6.jpg', '', '', 1, 1, 1, 0, 0, '2026-03-26 02:06:27.361318', '2026-03-26 02:06:27.361331', 11),
(7, 'Heavyweight Premium Tee', 'heavyweight-premium-tee', 'T-shirt premium en coton heavyweight 280g. Qualité supérieure.', 11000, NULL, 25, 'products/shirt7.jpg', '', '', 1, 0, 1, 0, 0, '2026-03-26 02:06:27.368599', '2026-03-26 02:06:27.368612', 11),
(8, 'Minimal Logo Tee', 'minimal-logo-tee', 'Logo minimal brodé sur poitrine. Style épuré et élégant.', 7500, NULL, 25, 'products/shirt8.jpg', '', '', 0, 1, 1, 0, 0, '2026-03-26 02:06:27.375781', '2026-03-26 02:06:27.375794', 11),
(9, 'Vintage Wash Tee', 'vintage-wash-tee', 'Lavage vintage pour un effet usé tendance. Unique et authentique.', 9000, 7000, 25, 'products/shirt9.jpg', '', '', 1, 1, 1, 1, 0, '2026-03-26 02:06:27.381996', '2026-03-26 02:06:27.382017', 11),
(10, 'Acid Wash Street Tee', 'acid-wash-street-tee', 'Effet acid wash pour un look streetwear audacieux et original.', 8500, NULL, 25, 'products/shirt10.jpg', '', '', 1, 1, 1, 0, 0, '2026-03-26 02:06:27.389775', '2026-03-26 02:06:27.389788', 11),
(11, 'Longline Urban Tee', 'longline-urban-tee', 'Coupe longline tombante, moderne et stylée pour les looks urbains.', 10000, NULL, 25, 'products/shirt11.jpg', '', '', 1, 0, 1, 0, 0, '2026-03-26 02:06:27.395829', '2026-03-26 02:06:27.395844', 11),
(12, 'Patchwork Tee Culture', 'patchwork-tee-culture', 'T-shirt patchwork culture avec détails couture exclusifs.', 12000, 9500, 25, 'products/shirt12.jpg', '', '', 1, 1, 1, 0, 0, '2026-03-26 02:06:27.403225', '2026-03-26 02:06:27.403238', 11),
(13, 'Half-Zip Street Tee', 'half-zip-street-tee', 'Half-zip avec col contrasté, design technique et streetwear.', 9500, NULL, 25, 'products/shirt13.jpg', '', '', 0, 1, 1, 0, 0, '2026-03-26 02:06:27.410350', '2026-03-26 02:06:27.410365', 11),
(14, 'Tie-Dye Street Edition', 'tie-dye-street-edition', 'Tie-dye street edition, chaque pièce est unique et artisanale.', 8000, NULL, 25, 'products/shirt14.jpg', '', '', 1, 1, 1, 0, 0, '2026-03-26 02:06:27.415497', '2026-03-26 02:06:27.415511', 11),
(15, 'Embroidered Logo Tee', 'embroidered-logo-tee', 'Logo brodé en fil or. La pièce signature de la collection.', 11000, 8500, 25, 'products/shirt15.jpg', '', '', 1, 0, 1, 1, 0, '2026-03-26 02:06:27.423037', '2026-03-26 02:06:27.423051', 11),
(16, 'Cut & Sew Urban Tee', 'cut-sew-urban-tee', 'Cut & sew avec coupes asymétriques pour un style avant-gardiste.', 13000, NULL, 25, 'products/shirt16.jpg', '', '', 1, 1, 1, 1, 0, '2026-03-26 02:06:27.429586', '2026-03-26 02:06:27.429609', 11),
(17, 'Signature TSW Tee', 'signature-tsw-tee', 'La pièce signature ThiamStreetwear. Logo TSW brodé au dos.', 10500, NULL, 25, 'products/shirt17.jpg', '', '', 1, 1, 1, 0, 0, '2026-03-26 02:06:27.435998', '2026-03-26 02:06:27.436013', 11),
(18, 'Air Street Low Black', 'air-street-low-black', 'Sneaker basse streetwear coloris noir. Semelle épaisse et confort premium.', 25000, 19500, 15, 'products/shoes_2.jpg', '', '', 1, 1, 1, 0, 0, '2026-03-26 02:15:27.705879', '2026-03-26 02:15:27.706116', 7),
(19, 'Urban Runner White', 'urban-runner-white', 'Runner urbain blanc immaculé. Légère et confortable pour le quotidien.', 22000, NULL, 15, 'products/shoes_3.jpg', '', '', 1, 1, 1, 0, 0, '2026-03-26 02:15:27.718573', '2026-03-26 02:15:27.718591', 7),
(20, 'Street Force Mid', 'street-force-mid', 'Sneaker mid-cut style street force. Tige renforcée et amorti optimal.', 28000, NULL, 15, 'products/shoes_4.jpg', '', '', 1, 0, 1, 0, 0, '2026-03-26 02:15:27.725771', '2026-03-26 02:15:27.725785', 7),
(21, 'Classic Court Low', 'classic-court-low', 'Court low classique indémodable. Polyvalent pour tous les looks.', 18000, 14500, 15, 'products/shoes_10.jpg', '', '', 0, 1, 1, 1, 0, '2026-03-26 02:15:27.736962', '2026-03-26 02:15:27.736979', 7),
(22, 'Premium Leather Sneaker', 'premium-leather-sneaker', 'Sneaker premium en cuir véritable. La pièce de collection par excellence.', 35000, NULL, 15, 'products/shoes_15.jpg', '', '', 1, 1, 1, 0, 0, '2026-03-26 02:15:27.745070', '2026-03-26 02:15:27.745082', 7),
(23, 'Cargo Street Pant', 'cargo-street-pant', 'Cargo streetwear avec poches latérales. Style militaire urbain.', 15000, NULL, 20, 'products/pants2.jpg', '', '', 1, 1, 1, 0, 0, '2026-03-26 02:15:27.753074', '2026-03-26 02:15:27.753090', 13),
(24, 'Jogger Urban Essential', 'jogger-urban-essential', 'Jogger confort avec bandes latérales. Idéal sport et casual.', 12000, 9500, 20, 'products/pants3.jpg', '', '', 0, 1, 1, 0, 0, '2026-03-26 02:15:27.760661', '2026-03-26 02:15:27.760673', 13),
(25, 'Slim Fit Street Trouser', 'slim-fit-street-trouser', 'Coupe slim fit moderne et épurée. Polyvalent pour toutes occasions.', 14000, NULL, 20, 'products/pants4.jpg', '', '', 1, 0, 1, 0, 0, '2026-03-26 02:15:27.766904', '2026-03-26 02:15:27.766919', 13),
(26, 'Wide Leg Baggy Pant', 'wide-leg-baggy-pant', 'Wide leg baggy tendance. Le pantalon statement de la saison.', 16000, NULL, 20, 'products/pants5.jpg', '', '', 1, 1, 1, 0, 0, '2026-03-26 02:15:27.772005', '2026-03-26 02:15:27.772023', 13),
(27, 'Track Pant Classic', 'track-pant-classic', 'Track pant classique avec bandes. Style sport et streetwear.', 11000, 8500, 20, 'products/pants6.jpg', '', '', 0, 0, 1, 0, 0, '2026-03-26 02:15:27.778926', '2026-03-26 02:15:27.778938', 13),
(28, 'Tactical Cargo Pant', 'tactical-cargo-pant', 'Cargo tactique avec multiples poches. Look utilitaire tendance.', 18000, NULL, 20, 'products/pants7.jpg', '', '', 1, 1, 1, 0, 0, '2026-03-26 02:15:27.785699', '2026-03-26 02:15:27.785714', 13),
(29, 'Relaxed Fit Denim Street', 'relaxed-fit-denim-street', 'Denim street coupe relaxed. Lavage vintage authentique.', 17000, 13500, 20, 'products/pants8.jpg', '', '', 1, 1, 1, 0, 0, '2026-03-26 02:15:27.790220', '2026-03-26 02:15:27.790232', 13),
(30, 'Corduroy Street Pant', 'corduroy-street-pant', 'Velours côtelé pour un look texturé et sophistiqué.', 16000, NULL, 20, 'products/pants9.jpg', '', '', 1, 0, 1, 0, 0, '2026-03-26 02:15:27.799373', '2026-03-26 02:15:27.799386', 13),
(31, 'Tech Fleece Street Pant', 'tech-fleece-street-pant', 'Tech fleece ultra-confort. Parfait pour un look sport-luxe.', 19000, NULL, 20, 'products/pants10.jpg', '', '', 1, 1, 1, 0, 0, '2026-03-26 02:15:27.804651', '2026-03-26 02:15:27.804666', 13),
(32, 'Beanie Street Noir', 'beanie-street-noir', 'Beanie streetwear en laine mélangée. Chaud et stylé pour l\'hiver dakarois.', 4500, NULL, 30, 'products/beanie.jpg', '', '', 1, 1, 1, 1, 0, '2026-03-26 02:15:27.810885', '2026-03-26 02:15:27.810899', 20),
(33, 'Beanie Oversize Ribbed', 'beanie-oversize-ribbed', 'Beanie oversize côtelé pour un look casual et confortable.', 5000, 3800, 30, 'products/beanie2.jpg', '', '', 1, 1, 1, 0, 0, '2026-03-26 02:15:27.817549', '2026-03-26 02:15:27.817565', 20),
(34, 'Beanie Pom-Pom Urban', 'beanie-pom-pom-urban', 'Beanie avec pompon. La touche tendance pour finaliser ton look street.', 5500, NULL, 30, 'products/beanie3.jpg', '', '', 1, 0, 1, 0, 0, '2026-03-26 02:15:27.823517', '2026-03-26 02:15:27.823538', 20),
(35, 'Jordan Street Low', 'jordan-street-low', 'Jordan Street Low — Collection ThiamStreetwear. Style urbain authentique pour les rues de Dakar.', 42000, 35000, 15, 'products/basket1.jpg', '', '', 1, 1, 1, 2, 22, '2026-03-26 03:10:54.988702', '2026-03-26 03:10:54.988742', 8),
(36, 'Air Force One Classic', 'air-force-one-classic', 'Air Force One Classic — Collection ThiamStreetwear. Style urbain authentique pour les rues de Dakar.', 38000, NULL, 20, 'products/basket2.jpg', '', '', 1, 0, 1, 0, 41, '2026-03-26 03:10:55.005809', '2026-03-26 03:10:55.005838', 8),
(37, 'Street Runner Pro', 'street-runner-pro', 'Street Runner Pro — Collection ThiamStreetwear. Style urbain authentique pour les rues de Dakar.', 29500, NULL, 10, 'products/basket3.jpg', '', '', 0, 1, 1, 0, 8, '2026-03-26 03:10:55.013346', '2026-03-26 03:10:55.013371', 8),
(38, 'Classic Low Top', 'classic-low-top', 'Classic Low Top — Collection ThiamStreetwear. Style urbain authentique pour les rues de Dakar.', 25000, NULL, 18, 'products/basket4.jpg', '', '', 0, 0, 1, 0, 15, '2026-03-26 03:10:55.018674', '2026-03-26 03:10:55.018699', 8),
(39, 'Urban Boots Dakar', 'urban-boots-dakar', 'Urban Boots Dakar — Collection ThiamStreetwear. Style urbain authentique pour les rues de Dakar.', 55000, NULL, 8, 'products/boot1.jpg', '', '', 1, 1, 1, 0, 12, '2026-03-26 03:10:55.033510', '2026-03-26 03:10:55.033530', 9),
(40, 'Desert Boot Sable', 'desert-boot-sable', 'Desert Boot Sable — Collection ThiamStreetwear. Style urbain authentique pour les rues de Dakar.', 48000, 40000, 12, 'products/boot2.jpg', '', '', 0, 0, 1, 0, 6, '2026-03-26 03:10:55.040387', '2026-03-26 03:10:55.040407', 9),
(41, 'Chelsea Boot Noir', 'chelsea-boot-noir', 'Chelsea Boot Noir — Collection ThiamStreetwear. Style urbain authentique pour les rues de Dakar.', 52000, NULL, 6, 'products/boot3.jpg', '', '', 0, 1, 1, 0, 9, '2026-03-26 03:10:55.045746', '2026-03-26 03:10:55.045765', 9),
(42, 'Slides Street Noir', 'slides-street-noir', 'Slides Street Noir — Collection ThiamStreetwear. Style urbain authentique pour les rues de Dakar.', 12000, NULL, 30, 'products/sandal1.jpg', '', '', 0, 1, 1, 0, 45, '2026-03-26 03:10:55.049879', '2026-03-26 03:10:55.049896', 10),
(43, 'Claquettes Logo TSW', 'claquettes-logo-tsw', 'Claquettes Logo TSW — Collection ThiamStreetwear. Style urbain authentique pour les rues de Dakar.', 9500, 7500, 25, 'products/sandal2.jpg', '', '', 1, 0, 1, 0, 38, '2026-03-26 03:10:55.052796', '2026-03-26 03:10:55.052811', 10),
(44, 'Sandales Sport Dakar', 'sandales-sport-dakar', 'Sandales Sport Dakar — Collection ThiamStreetwear. Style urbain authentique pour les rues de Dakar.', 15000, NULL, 14, 'products/sandal3.jpg', '', '', 0, 1, 1, 0, 7, '2026-03-26 03:10:55.055379', '2026-03-26 03:10:55.055390', 10),
(45, 'Hoodie TSW Oversize', 'hoodie-tsw-oversize', 'Hoodie TSW Oversize — Collection ThiamStreetwear. Style urbain authentique pour les rues de Dakar.', 28000, NULL, 20, 'products/hoodie1.jpg', '', '', 1, 1, 1, 1, 33, '2026-03-26 03:10:55.058214', '2026-03-26 03:10:55.058230', 12),
(46, 'Sweat Zippé Urban', 'sweat-zippe-urban', 'Sweat Zippé Urban — Collection ThiamStreetwear. Style urbain authentique pour les rues de Dakar.', 32000, 26000, 15, 'products/hoodie2.jpg', '', '', 0, 0, 1, 0, 18, '2026-03-26 03:10:55.061602', '2026-03-26 03:10:55.061620', 12),
(47, 'Hoodie Brodé Gold', 'hoodie-brode-gold', 'Hoodie Brodé Gold — Collection ThiamStreetwear. Style urbain authentique pour les rues de Dakar.', 35000, NULL, 10, 'products/hoodie3.jpg', '', '', 0, 1, 1, 1, 11, '2026-03-26 03:10:55.064509', '2026-03-26 03:10:55.064523', 12),
(48, 'Pull Streetwear Logo', 'pull-streetwear-logo', 'Pull Streetwear Logo — Collection ThiamStreetwear. Style urbain authentique pour les rues de Dakar.', 24000, NULL, 22, 'products/hoodie4.jpg', '', '', 0, 0, 1, 0, 14, '2026-03-26 03:10:55.067316', '2026-03-26 03:10:55.067331', 12),
(49, 'Sweat Capuche Oversize', 'sweat-capuche-oversize', 'Sweat Capuche Oversize — Collection ThiamStreetwear. Style urbain authentique pour les rues de Dakar.', 30000, NULL, 8, 'products/hoodie5.jpg', '', '', 0, 1, 1, 0, 5, '2026-03-26 03:10:55.070042', '2026-03-26 03:10:55.070056', 12),
(50, 'Veste Coach Noir', 'veste-coach-noir', 'Veste Coach Noir — Collection ThiamStreetwear. Style urbain authentique pour les rues de Dakar.', 45000, NULL, 12, 'products/veste_h1.jpg', '', '', 1, 1, 1, 0, 17, '2026-03-26 03:10:55.073664', '2026-03-26 03:10:55.073681', 14);

INSERT INTO `store_product` (`id`, `name`, `slug`, `description`, `price`, `discount_price`, `stock`, `image`, `image2`, `image3`, `is_featured`, `is_new`, `is_active`, `views_count`, `sales_count`, `created_at`, `updated_at`, `category_id`) VALUES
(51, 'Bomber Urban TSW', 'bomber-urban-tsw', 'Bomber Urban TSW — Collection ThiamStreetwear. Style urbain authentique pour les rues de Dakar.', 52000, 44000, 8, 'products/veste_h2.jpg', '', '', 0, 0, 1, 0, 24, '2026-03-26 03:10:55.076573', '2026-03-26 03:10:55.076588', 14),
(52, 'Veste Denim Streetwear', 'veste-denim-streetwear', 'Veste Denim Streetwear — Collection ThiamStreetwear. Style urbain authentique pour les rues de Dakar.', 38000, NULL, 10, 'products/veste_h3.jpg', '', '', 0, 1, 1, 0, 9, '2026-03-26 03:10:55.080458', '2026-03-26 03:10:55.080477', 14),
(53, 'Jacket Militaire Kaki', 'jacket-militaire-kaki', 'Jacket Militaire Kaki — Collection ThiamStreetwear. Style urbain authentique pour les rues de Dakar.', 48000, NULL, 6, 'products/veste_h4.jpg', '', '', 0, 0, 1, 0, 13, '2026-03-26 03:10:55.083587', '2026-03-26 03:10:55.083602', 14),
(54, 'Short Cargo Noir', 'short-cargo-noir', 'Short Cargo Noir — Collection ThiamStreetwear. Style urbain authentique pour les rues de Dakar.', 16500, NULL, 25, 'products/short1.jpg', '', '', 1, 1, 1, 0, 29, '2026-03-26 03:10:55.087971', '2026-03-26 03:10:55.087988', 15),
(55, 'Short Sport TSW', 'short-sport-tsw', 'Short Sport TSW — Collection ThiamStreetwear. Style urbain authentique pour les rues de Dakar.', 12000, 9500, 30, 'products/short2.jpg', '', '', 0, 0, 1, 1, 42, '2026-03-26 03:10:55.091370', '2026-03-26 03:10:55.091386', 15),
(56, 'Bermuda Streetwear', 'bermuda-streetwear', 'Bermuda Streetwear — Collection ThiamStreetwear. Style urbain authentique pour les rues de Dakar.', 14000, NULL, 18, 'products/short3.jpg', '', '', 0, 1, 1, 2, 11, '2026-03-26 03:10:55.094573', '2026-03-26 03:10:55.094591', 15),
(57, 'Short Jogging Urban', 'short-jogging-urban', 'Short Jogging Urban — Collection ThiamStreetwear. Style urbain authentique pour les rues de Dakar.', 11000, NULL, 22, 'products/short4.jpg', '', '', 0, 0, 1, 1, 16, '2026-03-26 03:10:55.097913', '2026-03-26 03:10:55.097928', 15),
(72, 'Sac à Dos Urban TSW', 'sac-a-dos-urban-tsw', 'Sac à Dos Urban TSW — Collection ThiamStreetwear. Style urbain authentique pour les rues de Dakar.', 25000, NULL, 15, 'products/sac1.jpg', '', '', 1, 1, 1, 0, 22, '2026-03-26 03:10:55.150706', '2026-03-26 03:10:55.150720', 21),
(73, 'Tote Bag Streetwear', 'tote-bag-streetwear', 'Tote Bag Streetwear — Collection ThiamStreetwear. Style urbain authentique pour les rues de Dakar.', 8500, NULL, 30, 'products/sac2.jpg', '', '', 0, 0, 1, 0, 47, '2026-03-26 03:10:55.153481', '2026-03-26 03:10:55.153497', 21),
(74, 'Sacoche Waist Bag', 'sacoche-waist-bag', 'Sacoche Waist Bag — Collection ThiamStreetwear. Style urbain authentique pour les rues de Dakar.', 18000, 14000, 20, 'products/sac3.jpg', '', '', 0, 1, 1, 0, 19, '2026-03-26 03:10:55.156069', '2026-03-26 03:10:55.156081', 21),
(75, 'Sneakers N°1', 'sneakers-n1', 'Sneakers de qualite premium, reference CHAUSSURES1. Disponible en plusieurs tailles. Livraison sur Dakar.', 25000, NULL, 10, 'products/sneakers_1_WhatsApp Image 2026-03-26 at 22.12.00.jpeg', 'products/sneakers_1_WhatsApp Image 2026-03-26 at 22.12.01.jpeg', 'products/sneakers_1_WhatsApp Image 2026-03-26 at 22.12.05.jpeg', 1, 1, 1, 0, 0, '2026-03-31 00:34:59.388322', '2026-03-31 00:34:59.388341', 7),
(76, 'Sneakers N°2', 'sneakers-n2', 'Sneakers de qualite premium, reference CHAUSSURES2. Disponible en plusieurs tailles. Livraison sur Dakar.', 25000, NULL, 10, 'products/sneakers_2_WhatsApp Image 2026-03-26 at 22.12.07.jpeg', 'products/sneakers_2_WhatsApp Image 2026-03-26 at 22.12.09.jpeg', 'products/sneakers_2_WhatsApp Image 2026-03-26 at 22.12.15.jpeg', 1, 1, 1, 0, 0, '2026-03-31 00:34:59.410560', '2026-03-31 00:34:59.410576', 7),
(77, 'Sneakers N°3', 'sneakers-n3', 'Sneakers de qualite premium, reference CHAUSSURES3. Disponible en plusieurs tailles. Livraison sur Dakar.', 25000, NULL, 10, 'products/sneakers_3_WhatsApp Image 2026-03-26 at 22.12.15 (1).jpeg', 'products/sneakers_3_WhatsApp Image 2026-03-26 at 22.12.31.jpeg', 'products/sneakers_3_WhatsApp Image 2026-03-26 at 22.12.33.jpeg', 1, 1, 1, 0, 0, '2026-03-31 00:34:59.425098', '2026-03-31 00:34:59.425112', 7),
(78, 'Sneakers N°4', 'sneakers-n4', 'Sneakers de qualite premium, reference CHAUSSURES4. Disponible en plusieurs tailles. Livraison sur Dakar.', 25000, NULL, 10, 'products/sneakers_4_WhatsApp Image 2026-03-26 at 22.12.41.jpeg', 'products/sneakers_4_WhatsApp Image 2026-03-26 at 22.12.43.jpeg', '', 1, 1, 1, 0, 0, '2026-03-31 00:34:59.438382', '2026-03-31 00:34:59.438395', 7),
(79, 'Sneakers N°5', 'sneakers-n5', 'Sneakers de qualite premium, reference CHAUSSURES5. Disponible en plusieurs tailles. Livraison sur Dakar.', 25000, NULL, 10, 'products/sneakers_5_WhatsApp Image 2026-03-26 at 22.12.47.jpeg', 'products/sneakers_5_WhatsApp Image 2026-03-26 at 22.12.49.jpeg', 'products/sneakers_5_WhatsApp Image 2026-03-26 at 22.12.51.jpeg', 1, 1, 1, 0, 0, '2026-03-31 00:34:59.453633', '2026-03-31 00:34:59.453648', 7),
(80, 'Sneakers N°6', 'sneakers-n6', 'Sneakers de qualite premium, reference CHAUSSURES6. Disponible en plusieurs tailles. Livraison sur Dakar.', 25000, NULL, 10, 'products/sneakers_6_WhatsApp Image 2026-03-26 at 22.12.53.jpeg', 'products/sneakers_6_WhatsApp Image 2026-03-26 at 22.12.54.jpeg', 'products/sneakers_6_WhatsApp Image 2026-03-26 at 22.12.55 (1).jpeg', 0, 1, 1, 1, 0, '2026-03-31 00:34:59.465473', '2026-03-31 00:34:59.465482', 7),
(81, 'Sneakers N°7', 'sneakers-n7', 'Sneakers de qualite premium, reference CHAUSSURES7. Disponible en plusieurs tailles. Livraison sur Dakar.', 25000, NULL, 10, 'products/sneakers_7_WhatsApp Image 2026-03-26 at 22.12.56 (1).jpeg', 'products/sneakers_7_WhatsApp Image 2026-03-26 at 22.12.56 (2).jpeg', 'products/sneakers_7_WhatsApp Image 2026-03-26 at 22.12.57 (1).jpeg', 0, 1, 1, 0, 0, '2026-03-31 00:34:59.499267', '2026-03-31 00:34:59.499282', 7),
(82, 'Sneakers N°8', 'sneakers-n8', 'Sneakers de qualite premium, reference CHAUSSURES8. Disponible en plusieurs tailles. Livraison sur Dakar.', 25000, NULL, 10, 'products/sneakers_8_WhatsApp Image 2026-03-26 at 22.12.58 (1).jpeg', 'products/sneakers_8_WhatsApp Image 2026-03-26 at 22.12.58.jpeg', '', 0, 1, 1, 0, 0, '2026-03-31 00:34:59.532918', '2026-03-31 00:34:59.532932', 7),
(83, 'Sneakers N°9', 'sneakers-n9', 'Sneakers de qualite premium, reference CHAUSSURES9. Disponible en plusieurs tailles. Livraison sur Dakar.', 25000, NULL, 10, 'products/sneakers_9_WhatsApp Image 2026-03-26 at 22.13.00 (1).jpeg', 'products/sneakers_9_WhatsApp Image 2026-03-26 at 22.13.00 (2).jpeg', 'products/sneakers_9_WhatsApp Image 2026-03-26 at 22.13.00.jpeg', 0, 1, 1, 0, 0, '2026-03-31 00:34:59.555575', '2026-03-31 00:34:59.555591', 7),
(84, 'Sneakers N°10', 'sneakers-n10', 'Sneakers de qualite premium, reference CHAUSSURES10. Disponible en plusieurs tailles. Livraison sur Dakar.', 25000, NULL, 10, 'products/sneakers_10_WhatsApp Image 2026-03-26 at 22.13.01.jpeg', 'products/sneakers_10_WhatsApp Image 2026-03-26 at 22.13.02 (2).jpeg', '', 0, 1, 1, 1, 0, '2026-03-31 00:34:59.571977', '2026-03-31 00:34:59.571991', 7),
(85, 'Sneakers N°11', 'sneakers-n11', 'Sneakers de qualite premium, reference CHAUSSURES11. Disponible en plusieurs tailles. Livraison sur Dakar.', 25000, NULL, 10, 'products/sneakers_11_WhatsApp Image 2026-03-26 at 22.13.02 (1).jpeg', 'products/sneakers_11_WhatsApp Image 2026-03-26 at 22.13.03 (1).jpeg', 'products/sneakers_11_WhatsApp Image 2026-03-26 at 22.13.03 (3).jpeg', 0, 1, 1, 1, 0, '2026-03-31 00:34:59.597780', '2026-03-31 00:34:59.597796', 7),
(86, 'Sneakers N°12', 'sneakers-n12', 'Sneakers de qualite premium, reference CHAUSSURES12. Disponible en plusieurs tailles. Livraison sur Dakar.', 25000, NULL, 10, 'products/sneakers_12_WhatsApp Image 2026-03-26 at 22.13.04 (1).jpeg', 'products/sneakers_12_WhatsApp Image 2026-03-26 at 22.13.05 (1).jpeg', 'products/sneakers_12_WhatsApp Image 2026-03-26 at 22.13.05.jpeg', 0, 1, 1, 0, 0, '2026-03-31 00:34:59.609405', '2026-03-31 00:34:59.609417', 7),
(87, 'Sneakers N°13', 'sneakers-n13', 'Sneakers de qualite premium, reference CHAUSSURES13. Disponible en plusieurs tailles. Livraison sur Dakar.', 25000, NULL, 10, 'products/sneakers_13_WhatsApp Image 2026-03-26 at 22.13.06 (2).jpeg', 'products/sneakers_13_WhatsApp Image 2026-03-26 at 22.13.07 (1).jpeg', 'products/sneakers_13_WhatsApp Image 2026-03-26 at 22.13.07.jpeg', 0, 1, 1, 0, 0, '2026-03-31 00:34:59.619532', '2026-03-31 00:34:59.619546', 7),
(88, 'Sneakers N°14', 'sneakers-n14', 'Sneakers de qualite premium, reference CHAUSSURES14. Disponible en plusieurs tailles. Livraison sur Dakar.', 25000, NULL, 10, 'products/sneakers_14_WhatsApp Image 2026-03-26 at 22.13.08 (1).jpeg', 'products/sneakers_14_WhatsApp Image 2026-03-26 at 22.13.09 (2).jpeg', 'products/sneakers_14_WhatsApp Image 2026-03-26 at 22.13.09.jpeg', 0, 1, 1, 0, 0, '2026-03-31 00:34:59.631587', '2026-03-31 00:34:59.631596', 7),
(89, 'Sneakers N°15', 'sneakers-n15', 'Sneakers de qualite premium, reference CHAUSSURES15. Disponible en plusieurs tailles. Livraison sur Dakar.', 25000, NULL, 10, 'products/sneakers_15_WhatsApp Image 2026-03-26 at 22.26.53 (1).jpeg', 'products/sneakers_15_WhatsApp Image 2026-03-26 at 22.26.53.jpeg', 'products/sneakers_15_WhatsApp Image 2026-03-26 at 22.26.54 (1).jpeg', 0, 1, 1, 1, 0, '2026-03-31 00:34:59.646526', '2026-03-31 00:34:59.646539', 7),
(90, 'Sneakers N°16', 'sneakers-n16', 'Sneakers de qualite premium, reference CHAUSSURES16. Disponible en plusieurs tailles. Livraison sur Dakar.', 25000, NULL, 10, 'products/sneakers_16_WhatsApp Image 2026-03-26 at 22.26.55 (2).jpeg', 'products/sneakers_16_WhatsApp Image 2026-03-26 at 22.26.55 (3).jpeg', 'products/sneakers_16_WhatsApp Image 2026-03-26 at 22.26.55 (4).jpeg', 0, 1, 1, 1, 0, '2026-03-31 00:34:59.662363', '2026-03-31 00:34:59.662373', 7),
(91, 'Sneakers N°17', 'sneakers-n17', 'Sneakers de qualite premium, reference CHAUSSURES17. Disponible en plusieurs tailles. Livraison sur Dakar.', 25000, NULL, 10, 'products/sneakers_17_WhatsApp Image 2026-03-26 at 22.26.58.jpeg', 'products/sneakers_17_WhatsApp Image 2026-03-26 at 22.26.59 (1).jpeg', 'products/sneakers_17_WhatsApp Image 2026-03-26 at 22.26.59.jpeg', 0, 1, 1, 0, 0, '2026-03-31 00:34:59.673613', '2026-03-31 00:34:59.673625', 7),
(92, 'Sneakers N°18', 'sneakers-n18', 'Sneakers de qualite premium, reference CHAUSSURES18. Disponible en plusieurs tailles. Livraison sur Dakar.', 25000, NULL, 9, 'products/sneakers_18_WhatsApp Image 2026-03-26 at 22.27.02 (1).jpeg', 'products/sneakers_18_WhatsApp Image 2026-03-26 at 22.27.02 (2).jpeg', 'products/sneakers_18_WhatsApp Image 2026-03-26 at 22.27.02.jpeg', 0, 1, 1, 0, 1, '2026-03-31 00:34:59.686919', '2026-03-31 00:34:59.686927', 7),
(93, 'Sneakers N°19', 'sneakers-n19', 'Sneakers de qualite premium, reference CHAUSSURES19. Disponible en plusieurs tailles. Livraison sur Dakar.', 25000, NULL, 10, 'products/sneakers_19_WhatsApp Image 2026-03-26 at 22.27.04 (1).jpeg', 'products/sneakers_19_WhatsApp Image 2026-03-26 at 22.27.05.jpeg', '', 0, 1, 1, 0, 0, '2026-03-31 00:34:59.695785', '2026-03-31 00:34:59.695795', 7),
(94, 'Sneakers N°20', 'sneakers-n20', 'Sneakers de qualite premium, reference CHAUSSURES20. Disponible en plusieurs tailles. Livraison sur Dakar.', 25000, NULL, 10, 'products/sneakers_20_WhatsApp Image 2026-03-26 at 22.27.06.jpeg', 'products/sneakers_20_WhatsApp Image 2026-03-26 at 22.27.07.jpeg', '', 0, 1, 1, 0, 0, '2026-03-31 00:34:59.708100', '2026-03-31 00:34:59.708109', 7),
(95, 'Sneakers N°21', 'sneakers-n21', 'Sneakers de qualite premium, reference CHAUSSURES21. Disponible en plusieurs tailles. Livraison sur Dakar.', 25000, NULL, 10, 'products/sneakers_21_WhatsApp Image 2026-03-26 at 22.27.08 (1).jpeg', 'products/sneakers_21_WhatsApp Image 2026-03-26 at 22.27.08.jpeg', '', 0, 1, 1, 3, 0, '2026-03-31 00:34:59.720432', '2026-03-31 00:34:59.720444', 7),
(96, 'Sneakers N°22', 'sneakers-n22', 'Sneakers de qualite premium, reference CHAUSSURES22. Disponible en plusieurs tailles. Livraison sur Dakar.', 25000, NULL, 10, 'products/sneakers_22_WhatsApp Image 2026-03-26 at 22.27.09.jpeg', 'products/sneakers_22_WhatsApp Image 2026-03-26 at 22.27.10.jpeg', '', 0, 1, 1, 1, 0, '2026-03-31 00:34:59.730494', '2026-03-31 00:34:59.730504', 7),
(97, 'Sneakers N°23', 'sneakers-n23', 'Sneakers de qualite premium, reference CHAUSSURES23. Disponible en plusieurs tailles. Livraison sur Dakar.', 25000, NULL, 10, 'products/sneakers_23_WhatsApp Image 2026-03-26 at 22.27.12.jpeg', 'products/sneakers_23_WhatsApp Image 2026-03-26 at 22.27.13 (1).jpeg', 'products/sneakers_23_WhatsApp Image 2026-03-26 at 22.27.13.jpeg', 0, 1, 1, 1, 0, '2026-03-31 00:34:59.747982', '2026-03-31 00:34:59.747993', 7);

-- --------------------------------------------------------

--
-- Structure de la table `store_productreview`
--

CREATE TABLE `store_productreview` (
  `id` bigint(20) NOT NULL,
  `rating` int(11) NOT NULL,
  `comment` longtext NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `product_id` bigint(20) NOT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Chargement des donnees de la table `store_productreview`
--


-- --------------------------------------------------------

--
-- Structure de la table `store_product_colors`
--

CREATE TABLE `store_product_colors` (
  `id` bigint(20) NOT NULL,
  `product_id` bigint(20) NOT NULL,
  `color_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Chargement des donnees de la table `store_product_colors`
--

INSERT INTO `store_product_colors` (`id`, `product_id`, `color_id`) VALUES
(1, 1, 1),
(2, 1, 2),
(3, 1, 3),
(4, 2, 1),
(5, 2, 2),
(6, 2, 3),
(7, 3, 1),
(8, 3, 2),
(9, 3, 3),
(10, 4, 1),
(11, 4, 2),
(12, 4, 3),
(13, 5, 1),
(14, 5, 2),
(15, 5, 3),
(16, 6, 1),
(17, 6, 2),
(18, 6, 3),
(19, 7, 1),
(20, 7, 2),
(21, 7, 3),
(22, 8, 1),
(23, 8, 2),
(24, 8, 3),
(25, 9, 1),
(26, 9, 2),
(27, 9, 3),
(28, 10, 1),
(29, 10, 2),
(30, 10, 3),
(31, 11, 1),
(32, 11, 2),
(33, 11, 3),
(34, 12, 1),
(35, 12, 2),
(36, 12, 3),
(37, 13, 1),
(38, 13, 2),
(39, 13, 3),
(40, 14, 1),
(41, 14, 2),
(42, 14, 3),
(43, 15, 1),
(44, 15, 2),
(45, 15, 3),
(46, 16, 1),
(47, 16, 2),
(48, 16, 3),
(49, 17, 1),
(50, 17, 2);

INSERT INTO `store_product_colors` (`id`, `product_id`, `color_id`) VALUES
(51, 17, 3),
(52, 18, 1),
(53, 18, 2),
(54, 18, 3),
(55, 19, 1),
(56, 19, 2),
(57, 19, 3),
(58, 20, 1),
(59, 20, 2),
(60, 20, 3),
(61, 21, 1),
(62, 21, 2),
(63, 21, 3),
(64, 22, 1),
(65, 22, 2),
(66, 22, 3),
(67, 23, 1),
(68, 23, 2),
(69, 23, 3),
(70, 24, 1),
(71, 24, 2),
(72, 24, 3),
(73, 25, 1),
(74, 25, 2),
(75, 25, 3),
(76, 26, 1),
(77, 26, 2),
(78, 26, 3),
(79, 27, 1),
(80, 27, 2),
(81, 27, 3),
(82, 28, 1),
(83, 28, 2),
(84, 28, 3),
(85, 29, 1),
(86, 29, 2),
(87, 29, 3),
(88, 30, 1),
(89, 30, 2),
(90, 30, 3),
(91, 31, 1),
(92, 31, 2),
(93, 31, 3),
(94, 32, 1),
(95, 32, 2),
(96, 32, 3),
(97, 33, 1),
(98, 33, 2),
(99, 33, 3),
(100, 34, 1);

INSERT INTO `store_product_colors` (`id`, `product_id`, `color_id`) VALUES
(101, 34, 2),
(102, 34, 3),
(103, 35, 1),
(104, 35, 2),
(105, 36, 1),
(106, 36, 2),
(107, 37, 1),
(108, 37, 3),
(109, 38, 2),
(110, 38, 5),
(111, 39, 1),
(112, 39, 10),
(113, 40, 9),
(114, 40, 10),
(115, 41, 1),
(116, 42, 1),
(117, 42, 2),
(118, 43, 1),
(119, 43, 3),
(120, 44, 1),
(121, 44, 5),
(122, 45, 1),
(123, 45, 3),
(124, 46, 1),
(125, 46, 6),
(126, 47, 1),
(127, 48, 9),
(128, 48, 3),
(129, 49, 8),
(130, 49, 1),
(131, 50, 1),
(132, 51, 8),
(133, 51, 1),
(134, 52, 1),
(135, 52, 5),
(136, 53, 8),
(137, 53, 7),
(138, 54, 8),
(139, 54, 1),
(140, 55, 1),
(141, 55, 3),
(142, 55, 5),
(143, 56, 8),
(144, 56, 9),
(145, 57, 1),
(146, 57, 4),
(176, 72, 1),
(177, 72, 3),
(178, 73, 1),
(179, 73, 2);

INSERT INTO `store_product_colors` (`id`, `product_id`, `color_id`) VALUES
(180, 73, 9),
(181, 74, 8),
(182, 74, 1);

-- --------------------------------------------------------

--
-- Structure de la table `store_product_sizes`
--

CREATE TABLE `store_product_sizes` (
  `id` bigint(20) NOT NULL,
  `product_id` bigint(20) NOT NULL,
  `size_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Chargement des donnees de la table `store_product_sizes`
--

INSERT INTO `store_product_sizes` (`id`, `product_id`, `size_id`) VALUES
(1, 1, 2),
(2, 1, 3),
(3, 1, 4),
(4, 1, 5),
(5, 1, 6),
(6, 2, 2),
(7, 2, 3),
(8, 2, 4),
(9, 2, 5),
(10, 2, 6),
(11, 3, 2),
(12, 3, 3),
(13, 3, 4),
(14, 3, 5),
(15, 3, 6),
(16, 4, 2),
(17, 4, 3),
(18, 4, 4),
(19, 4, 5),
(20, 4, 6),
(21, 5, 2),
(22, 5, 3),
(23, 5, 4),
(24, 5, 5),
(25, 5, 6),
(26, 6, 2),
(27, 6, 3),
(28, 6, 4),
(29, 6, 5),
(30, 6, 6),
(31, 7, 2),
(32, 7, 3),
(33, 7, 4),
(34, 7, 5),
(35, 7, 6),
(36, 8, 2),
(37, 8, 3),
(38, 8, 4),
(39, 8, 5),
(40, 8, 6),
(41, 9, 2),
(42, 9, 3),
(43, 9, 4),
(44, 9, 5),
(45, 9, 6),
(46, 10, 2),
(47, 10, 3),
(48, 10, 4),
(49, 10, 5),
(50, 10, 6);

INSERT INTO `store_product_sizes` (`id`, `product_id`, `size_id`) VALUES
(51, 11, 2),
(52, 11, 3),
(53, 11, 4),
(54, 11, 5),
(55, 11, 6),
(56, 12, 2),
(57, 12, 3),
(58, 12, 4),
(59, 12, 5),
(60, 12, 6),
(61, 13, 2),
(62, 13, 3),
(63, 13, 4),
(64, 13, 5),
(65, 13, 6),
(66, 14, 2),
(67, 14, 3),
(68, 14, 4),
(69, 14, 5),
(70, 14, 6),
(71, 15, 2),
(72, 15, 3),
(73, 15, 4),
(74, 15, 5),
(75, 15, 6),
(76, 16, 2),
(77, 16, 3),
(78, 16, 4),
(79, 16, 5),
(80, 16, 6),
(81, 17, 2),
(82, 17, 3),
(83, 17, 4),
(84, 17, 5),
(85, 17, 6),
(86, 18, 9),
(87, 18, 10),
(88, 18, 11),
(89, 18, 12),
(90, 18, 13),
(91, 18, 14),
(92, 18, 15),
(93, 18, 16),
(94, 19, 9),
(95, 19, 10),
(96, 19, 11),
(97, 19, 12),
(98, 19, 13),
(99, 19, 14),
(100, 19, 15);

INSERT INTO `store_product_sizes` (`id`, `product_id`, `size_id`) VALUES
(101, 19, 16),
(102, 20, 9),
(103, 20, 10),
(104, 20, 11),
(105, 20, 12),
(106, 20, 13),
(107, 20, 14),
(108, 20, 15),
(109, 20, 16),
(110, 21, 9),
(111, 21, 10),
(112, 21, 11),
(113, 21, 12),
(114, 21, 13),
(115, 21, 14),
(116, 21, 15),
(117, 21, 16),
(118, 22, 9),
(119, 22, 10),
(120, 22, 11),
(121, 22, 12),
(122, 22, 13),
(123, 22, 14),
(124, 22, 15),
(125, 22, 16),
(126, 23, 2),
(127, 23, 3),
(128, 23, 4),
(129, 23, 5),
(130, 23, 6),
(131, 24, 2),
(132, 24, 3),
(133, 24, 4),
(134, 24, 5),
(135, 24, 6),
(136, 25, 2),
(137, 25, 3),
(138, 25, 4),
(139, 25, 5),
(140, 25, 6),
(141, 26, 2),
(142, 26, 3),
(143, 26, 4),
(144, 26, 5),
(145, 26, 6),
(146, 27, 2),
(147, 27, 3),
(148, 27, 4),
(149, 27, 5),
(150, 27, 6);

INSERT INTO `store_product_sizes` (`id`, `product_id`, `size_id`) VALUES
(151, 28, 2),
(152, 28, 3),
(153, 28, 4),
(154, 28, 5),
(155, 28, 6),
(156, 29, 2),
(157, 29, 3),
(158, 29, 4),
(159, 29, 5),
(160, 29, 6),
(161, 30, 2),
(162, 30, 3),
(163, 30, 4),
(164, 30, 5),
(165, 30, 6),
(166, 31, 2),
(167, 31, 3),
(168, 31, 4),
(169, 31, 5),
(170, 31, 6),
(171, 32, 17),
(172, 33, 17),
(173, 34, 17),
(174, 35, 9),
(175, 35, 10),
(176, 35, 11),
(177, 35, 12),
(178, 35, 13),
(179, 35, 14),
(180, 36, 10),
(181, 36, 11),
(182, 36, 12),
(183, 36, 13),
(184, 36, 14),
(185, 36, 15),
(186, 37, 9),
(187, 37, 10),
(188, 37, 11),
(189, 37, 12),
(190, 37, 13),
(191, 38, 10),
(192, 38, 11),
(193, 38, 12),
(194, 38, 13),
(195, 38, 14),
(196, 39, 10),
(197, 39, 11),
(198, 39, 12),
(199, 39, 13),
(200, 39, 14);

INSERT INTO `store_product_sizes` (`id`, `product_id`, `size_id`) VALUES
(201, 39, 15),
(202, 40, 11),
(203, 40, 12),
(204, 40, 13),
(205, 40, 14),
(206, 41, 10),
(207, 41, 11),
(208, 41, 12),
(209, 41, 13),
(210, 41, 14),
(211, 41, 15),
(212, 42, 9),
(213, 42, 10),
(214, 42, 11),
(215, 42, 12),
(216, 42, 13),
(217, 42, 14),
(218, 42, 15),
(219, 43, 9),
(220, 43, 10),
(221, 43, 11),
(222, 43, 12),
(223, 43, 13),
(224, 43, 14),
(225, 44, 10),
(226, 44, 11),
(227, 44, 12),
(228, 44, 13),
(229, 45, 2),
(230, 45, 3),
(231, 45, 4),
(232, 45, 5),
(233, 45, 6),
(234, 46, 2),
(235, 46, 3),
(236, 46, 4),
(237, 46, 5),
(238, 47, 3),
(239, 47, 4),
(240, 47, 5),
(241, 47, 6),
(242, 48, 2),
(243, 48, 3),
(244, 48, 4),
(245, 48, 5),
(246, 49, 2),
(247, 49, 3),
(248, 49, 4),
(249, 49, 5),
(250, 49, 6);

INSERT INTO `store_product_sizes` (`id`, `product_id`, `size_id`) VALUES
(251, 50, 2),
(252, 50, 3),
(253, 50, 4),
(254, 50, 5),
(255, 51, 3),
(256, 51, 4),
(257, 51, 5),
(258, 51, 6),
(259, 52, 2),
(260, 52, 3),
(261, 52, 4),
(262, 52, 5),
(263, 53, 3),
(264, 53, 4),
(265, 53, 5),
(266, 54, 2),
(267, 54, 3),
(268, 54, 4),
(269, 54, 5),
(270, 55, 2),
(271, 55, 3),
(272, 55, 4),
(273, 55, 5),
(274, 55, 6),
(275, 56, 3),
(276, 56, 4),
(277, 56, 5),
(278, 57, 2),
(279, 57, 3),
(280, 57, 4),
(281, 57, 5),
(282, 57, 6),
(341, 72, 17),
(342, 73, 17),
(343, 74, 17),
(344, 75, 10),
(345, 75, 11),
(346, 75, 12),
(347, 75, 13),
(348, 75, 14),
(349, 75, 15),
(350, 75, 16),
(351, 76, 10),
(352, 76, 11),
(353, 76, 12),
(354, 76, 13),
(355, 76, 14),
(356, 76, 15),
(357, 76, 16),
(358, 77, 10);

INSERT INTO `store_product_sizes` (`id`, `product_id`, `size_id`) VALUES
(359, 77, 11),
(360, 77, 12),
(361, 77, 13),
(362, 77, 14),
(363, 77, 15),
(364, 77, 16),
(365, 78, 10),
(366, 78, 11),
(367, 78, 12),
(368, 78, 13),
(369, 78, 14),
(370, 78, 15),
(371, 78, 16),
(372, 79, 10),
(373, 79, 11),
(374, 79, 12),
(375, 79, 13),
(376, 79, 14),
(377, 79, 15),
(378, 79, 16),
(379, 80, 10),
(380, 80, 11),
(381, 80, 12),
(382, 80, 13),
(383, 80, 14),
(384, 80, 15),
(385, 80, 16),
(386, 81, 10),
(387, 81, 11),
(388, 81, 12),
(389, 81, 13),
(390, 81, 14),
(391, 81, 15),
(392, 81, 16),
(393, 82, 10),
(394, 82, 11),
(395, 82, 12),
(396, 82, 13),
(397, 82, 14),
(398, 82, 15),
(399, 82, 16),
(400, 83, 10),
(401, 83, 11),
(402, 83, 12),
(403, 83, 13),
(404, 83, 14),
(405, 83, 15),
(406, 83, 16),
(407, 84, 10),
(408, 84, 11);

INSERT INTO `store_product_sizes` (`id`, `product_id`, `size_id`) VALUES
(409, 84, 12),
(410, 84, 13),
(411, 84, 14),
(412, 84, 15),
(413, 84, 16),
(414, 85, 10),
(415, 85, 11),
(416, 85, 12),
(417, 85, 13),
(418, 85, 14),
(419, 85, 15),
(420, 85, 16),
(421, 86, 10),
(422, 86, 11),
(423, 86, 12),
(424, 86, 13),
(425, 86, 14),
(426, 86, 15),
(427, 86, 16),
(428, 87, 10),
(429, 87, 11),
(430, 87, 12),
(431, 87, 13),
(432, 87, 14),
(433, 87, 15),
(434, 87, 16),
(435, 88, 10),
(436, 88, 11),
(437, 88, 12),
(438, 88, 13),
(439, 88, 14),
(440, 88, 15),
(441, 88, 16),
(442, 89, 10),
(443, 89, 11),
(444, 89, 12),
(445, 89, 13),
(446, 89, 14),
(447, 89, 15),
(448, 89, 16),
(449, 90, 10),
(450, 90, 11),
(451, 90, 12),
(452, 90, 13),
(453, 90, 14),
(454, 90, 15),
(455, 90, 16),
(456, 91, 10),
(457, 91, 11),
(458, 91, 12);

INSERT INTO `store_product_sizes` (`id`, `product_id`, `size_id`) VALUES
(459, 91, 13),
(460, 91, 14),
(461, 91, 15),
(462, 91, 16),
(463, 92, 10),
(464, 92, 11),
(465, 92, 12),
(466, 92, 13),
(467, 92, 14),
(468, 92, 15),
(469, 92, 16),
(470, 93, 10),
(471, 93, 11),
(472, 93, 12),
(473, 93, 13),
(474, 93, 14),
(475, 93, 15),
(476, 93, 16),
(477, 94, 10),
(478, 94, 11),
(479, 94, 12),
(480, 94, 13),
(481, 94, 14),
(482, 94, 15),
(483, 94, 16),
(484, 95, 10),
(485, 95, 11),
(486, 95, 12),
(487, 95, 13),
(488, 95, 14),
(489, 95, 15),
(490, 95, 16),
(491, 96, 10),
(492, 96, 11),
(493, 96, 12),
(494, 96, 13),
(495, 96, 14),
(496, 96, 15),
(497, 96, 16),
(498, 97, 10),
(499, 97, 11),
(500, 97, 12),
(501, 97, 13),
(502, 97, 14),
(503, 97, 15),
(504, 97, 16);

-- --------------------------------------------------------

--
-- Structure de la table `store_size`
--

CREATE TABLE `store_size` (
  `id` bigint(20) NOT NULL,
  `name` varchar(20) NOT NULL,
  `order` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Chargement des donnees de la table `store_size`
--

INSERT INTO `store_size` (`id`, `name`, `order`) VALUES
(1, 'XS', 1),
(2, 'S', 2),
(3, 'M', 3),
(4, 'L', 4),
(5, 'XL', 5),
(6, 'XXL', 6),
(7, '36', 10),
(8, '37', 11),
(9, '38', 12),
(10, '39', 13),
(11, '40', 14),
(12, '41', 15),
(13, '42', 16),
(14, '43', 17),
(15, '44', 18),
(16, '45', 19),
(17, 'TU', 20);

-- --------------------------------------------------------

--
-- Structure de la table `store_wishlist`
--

CREATE TABLE `store_wishlist` (
  `id` bigint(20) NOT NULL,
  `added_at` datetime(6) NOT NULL,
  `product_id` bigint(20) NOT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Chargement des donnees de la table `store_wishlist`
--

INSERT INTO `store_wishlist` (`id`, `added_at`, `product_id`, `user_id`) VALUES
(1, '2026-03-26 03:30:36.558705', 21, 1),
(3, '2026-06-06 22:31:56.318709', 96, 3);

--
ALTER TABLE `accounts_profile`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `user_id` (`user_id`);

--
-- Index pour la table `account_emailaddress`
--
ALTER TABLE `account_emailaddress`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `account_emailaddress_user_id_email_987c8728_uniq` (`user_id`,`email`),
  ADD KEY `account_emailaddress_email_03be32b2` (`email`);

--
-- Index pour la table `account_emailconfirmation`
--
ALTER TABLE `account_emailconfirmation`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `key` (`key`),
  ADD KEY `account_emailconfirm_email_address_id_5b7f8c58_fk_account_e` (`email_address_id`);

--
-- Index pour la table `auth_group`
--
ALTER TABLE `auth_group`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- Index pour la table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  ADD KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`);

--
-- Index pour la table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`);

--
-- Index pour la table `auth_user`
--
ALTER TABLE `auth_user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`);

--
-- Index pour la table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  ADD KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`);

--
-- Index pour la table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  ADD KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`);

--
-- Index pour la table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD PRIMARY KEY (`id`),
  ADD KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  ADD KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`);

--
-- Index pour la table `django_content_type`
--
ALTER TABLE `django_content_type`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`);

--
-- Index pour la table `django_migrations`
--
ALTER TABLE `django_migrations`
  ADD PRIMARY KEY (`id`);

--
-- Index pour la table `django_session`
--
ALTER TABLE `django_session`
  ADD PRIMARY KEY (`session_key`),
  ADD KEY `django_session_expire_date_a5c62663` (`expire_date`);

--
-- Index pour la table `orders_cart`
--
ALTER TABLE `orders_cart`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `user_id` (`user_id`);

--
-- Index pour la table `orders_cartitem`
--
ALTER TABLE `orders_cartitem`
  ADD PRIMARY KEY (`id`),
  ADD KEY `orders_cartitem_cart_id_529df5fa_fk_orders_cart_id` (`cart_id`),
  ADD KEY `orders_cartitem_color_id_0772bf63_fk_store_color_id` (`color_id`),
  ADD KEY `orders_cartitem_product_id_55063ee7_fk_store_product_id` (`product_id`),
  ADD KEY `orders_cartitem_size_id_1ea4d069_fk_store_size_id` (`size_id`);

--
-- Index pour la table `orders_order`
--
ALTER TABLE `orders_order`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `order_number` (`order_number`),
  ADD KEY `orders_order_user_id_e9b59eb1_fk_auth_user_id` (`user_id`);

--
-- Index pour la table `orders_orderitem`
--
ALTER TABLE `orders_orderitem`
  ADD PRIMARY KEY (`id`),
  ADD KEY `orders_orderitem_color_id_df5636e7_fk_store_color_id` (`color_id`),
  ADD KEY `orders_orderitem_product_id_afe4254a_fk_store_product_id` (`product_id`),
  ADD KEY `orders_orderitem_size_id_c830e64a_fk_store_size_id` (`size_id`);

--
-- Index pour la table `orders_order_items`
--
ALTER TABLE `orders_order_items`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `orders_order_items_order_id_orderitem_id_9178d9f1_uniq` (`order_id`,`orderitem_id`),
  ADD KEY `orders_order_items_orderitem_id_97c0b6c4_fk_orders_orderitem_id` (`orderitem_id`);

--
-- Index pour la table `payments_payment`
--
ALTER TABLE `payments_payment`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `order_id` (`order_id`);

--
-- Index pour la table `socialaccount_socialaccount`
--
ALTER TABLE `socialaccount_socialaccount`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `socialaccount_socialaccount_provider_uid_fc810c6e_uniq` (`provider`,`uid`),
  ADD KEY `socialaccount_socialaccount_user_id_8146e70c_fk_auth_user_id` (`user_id`);

--
-- Index pour la table `socialaccount_socialapp`
--
ALTER TABLE `socialaccount_socialapp`
  ADD PRIMARY KEY (`id`);

--
-- Index pour la table `socialaccount_socialtoken`
--
ALTER TABLE `socialaccount_socialtoken`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `socialaccount_socialtoken_app_id_account_id_fca4e0ac_uniq` (`app_id`,`account_id`),
  ADD KEY `socialaccount_social_account_id_951f210e_fk_socialacc` (`account_id`);

--
-- Index pour la table `store_banner`
--
ALTER TABLE `store_banner`
  ADD PRIMARY KEY (`id`);

--
-- Index pour la table `store_category`
--
ALTER TABLE `store_category`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `slug` (`slug`),
  ADD KEY `store_category_parent_id_a6e736ff_fk_store_category_id` (`parent_id`);

--
-- Index pour la table `store_color`
--
ALTER TABLE `store_color`
  ADD PRIMARY KEY (`id`);

--
-- Index pour la table `store_product`
--
ALTER TABLE `store_product`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `slug` (`slug`),
  ADD KEY `store_product_category_id_574bae65_fk_store_category_id` (`category_id`);

--
-- Index pour la table `store_productreview`
--
ALTER TABLE `store_productreview`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `store_productreview_product_id_user_id_364c2620_uniq` (`product_id`,`user_id`),
  ADD KEY `store_productreview_user_id_7aa47bd8_fk_auth_user_id` (`user_id`);

--
-- Index pour la table `store_product_colors`
--
ALTER TABLE `store_product_colors`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `store_product_colors_product_id_color_id_cadfaf4e_uniq` (`product_id`,`color_id`),
  ADD KEY `store_product_colors_color_id_24fc7ccb_fk_store_color_id` (`color_id`);

--
-- Index pour la table `store_product_sizes`
--
ALTER TABLE `store_product_sizes`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `store_product_sizes_product_id_size_id_ae970894_uniq` (`product_id`,`size_id`),
  ADD KEY `store_product_sizes_size_id_fad63358_fk_store_size_id` (`size_id`);

--
-- Index pour la table `store_size`
--
ALTER TABLE `store_size`
  ADD PRIMARY KEY (`id`);

--
-- Index pour la table `store_wishlist`
--
ALTER TABLE `store_wishlist`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `store_wishlist_user_id_product_id_bcc1ac25_uniq` (`user_id`,`product_id`),
  ADD KEY `store_wishlist_product_id_8af1333d_fk_store_product_id` (`product_id`);

--
-- AUTO_INCREMENT pour les tables déchargées
--

--
-- AUTO_INCREMENT pour la table `accounts_profile`
--
ALTER TABLE `accounts_profile`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT pour la table `account_emailaddress`
--
ALTER TABLE `account_emailaddress`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT pour la table `account_emailconfirmation`
--
ALTER TABLE `account_emailconfirmation`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT pour la table `auth_group`
--
ALTER TABLE `auth_group`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT pour la table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT pour la table `auth_permission`
--
ALTER TABLE `auth_permission`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=97;

--
-- AUTO_INCREMENT pour la table `auth_user`
--
ALTER TABLE `auth_user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT pour la table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT pour la table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT pour la table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT pour la table `django_content_type`
--
ALTER TABLE `django_content_type`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=25;

--
-- AUTO_INCREMENT pour la table `django_migrations`
--
ALTER TABLE `django_migrations`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=38;

--
-- AUTO_INCREMENT pour la table `orders_cart`
--
ALTER TABLE `orders_cart`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT pour la table `orders_cartitem`
--
ALTER TABLE `orders_cartitem`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT pour la table `orders_order`
--
ALTER TABLE `orders_order`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT pour la table `orders_orderitem`
--
ALTER TABLE `orders_orderitem`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT pour la table `orders_order_items`
--
ALTER TABLE `orders_order_items`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT pour la table `payments_payment`
--
ALTER TABLE `payments_payment`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT pour la table `socialaccount_socialaccount`
--
ALTER TABLE `socialaccount_socialaccount`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT pour la table `socialaccount_socialapp`
--
ALTER TABLE `socialaccount_socialapp`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT pour la table `socialaccount_socialtoken`
--
ALTER TABLE `socialaccount_socialtoken`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT pour la table `store_banner`
--
ALTER TABLE `store_banner`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT pour la table `store_category`
--
ALTER TABLE `store_category`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=24;

--
-- AUTO_INCREMENT pour la table `store_color`
--
ALTER TABLE `store_color`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=16;

--
-- AUTO_INCREMENT pour la table `store_product`
--
ALTER TABLE `store_product`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=99;

--
-- AUTO_INCREMENT pour la table `store_productreview`
--
ALTER TABLE `store_productreview`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT pour la table `store_product_colors`
--
ALTER TABLE `store_product_colors`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=185;

--
-- AUTO_INCREMENT pour la table `store_product_sizes`
--
ALTER TABLE `store_product_sizes`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=522;

--
-- AUTO_INCREMENT pour la table `store_size`
--
ALTER TABLE `store_size`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=18;

--
-- AUTO_INCREMENT pour la table `store_wishlist`
--
ALTER TABLE `store_wishlist`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- Contraintes pour les tables déchargées
--

--
-- Contraintes pour la table `accounts_profile`
--
ALTER TABLE `accounts_profile`
  ADD CONSTRAINT `accounts_profile_user_id_49a85d32_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Contraintes pour la table `account_emailaddress`
--
ALTER TABLE `account_emailaddress`
  ADD CONSTRAINT `account_emailaddress_user_id_2c513194_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Contraintes pour la table `account_emailconfirmation`
--
ALTER TABLE `account_emailconfirmation`
  ADD CONSTRAINT `account_emailconfirm_email_address_id_5b7f8c58_fk_account_e` FOREIGN KEY (`email_address_id`) REFERENCES `account_emailaddress` (`id`);

--
-- Contraintes pour la table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);

--
-- Contraintes pour la table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

--
-- Contraintes pour la table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  ADD CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Contraintes pour la table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Contraintes pour la table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  ADD CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Contraintes pour la table `orders_cart`
--
ALTER TABLE `orders_cart`
  ADD CONSTRAINT `orders_cart_user_id_121a069e_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Contraintes pour la table `orders_cartitem`
--
ALTER TABLE `orders_cartitem`
  ADD CONSTRAINT `orders_cartitem_cart_id_529df5fa_fk_orders_cart_id` FOREIGN KEY (`cart_id`) REFERENCES `orders_cart` (`id`),
  ADD CONSTRAINT `orders_cartitem_color_id_0772bf63_fk_store_color_id` FOREIGN KEY (`color_id`) REFERENCES `store_color` (`id`),
  ADD CONSTRAINT `orders_cartitem_product_id_55063ee7_fk_store_product_id` FOREIGN KEY (`product_id`) REFERENCES `store_product` (`id`),
  ADD CONSTRAINT `orders_cartitem_size_id_1ea4d069_fk_store_size_id` FOREIGN KEY (`size_id`) REFERENCES `store_size` (`id`);

--
-- Contraintes pour la table `orders_order`
--
ALTER TABLE `orders_order`
  ADD CONSTRAINT `orders_order_user_id_e9b59eb1_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Contraintes pour la table `orders_orderitem`
--
ALTER TABLE `orders_orderitem`
  ADD CONSTRAINT `orders_orderitem_color_id_df5636e7_fk_store_color_id` FOREIGN KEY (`color_id`) REFERENCES `store_color` (`id`),
  ADD CONSTRAINT `orders_orderitem_product_id_afe4254a_fk_store_product_id` FOREIGN KEY (`product_id`) REFERENCES `store_product` (`id`),
  ADD CONSTRAINT `orders_orderitem_size_id_c830e64a_fk_store_size_id` FOREIGN KEY (`size_id`) REFERENCES `store_size` (`id`);

--
-- Contraintes pour la table `orders_order_items`
--
ALTER TABLE `orders_order_items`
  ADD CONSTRAINT `orders_order_items_order_id_ffafb841_fk_orders_order_id` FOREIGN KEY (`order_id`) REFERENCES `orders_order` (`id`),
  ADD CONSTRAINT `orders_order_items_orderitem_id_97c0b6c4_fk_orders_orderitem_id` FOREIGN KEY (`orderitem_id`) REFERENCES `orders_orderitem` (`id`);

--
-- Contraintes pour la table `payments_payment`
--
ALTER TABLE `payments_payment`
  ADD CONSTRAINT `payments_payment_order_id_22c479b7_fk_orders_order_id` FOREIGN KEY (`order_id`) REFERENCES `orders_order` (`id`);

--
-- Contraintes pour la table `socialaccount_socialaccount`
--
ALTER TABLE `socialaccount_socialaccount`
  ADD CONSTRAINT `socialaccount_socialaccount_user_id_8146e70c_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Contraintes pour la table `socialaccount_socialtoken`
--
ALTER TABLE `socialaccount_socialtoken`
  ADD CONSTRAINT `socialaccount_social_account_id_951f210e_fk_socialacc` FOREIGN KEY (`account_id`) REFERENCES `socialaccount_socialaccount` (`id`),
  ADD CONSTRAINT `socialaccount_social_app_id_636a42d7_fk_socialacc` FOREIGN KEY (`app_id`) REFERENCES `socialaccount_socialapp` (`id`);

--
-- Contraintes pour la table `store_category`
--
ALTER TABLE `store_category`
  ADD CONSTRAINT `store_category_parent_id_a6e736ff_fk_store_category_id` FOREIGN KEY (`parent_id`) REFERENCES `store_category` (`id`);

--
-- Contraintes pour la table `store_product`
--
ALTER TABLE `store_product`
  ADD CONSTRAINT `store_product_category_id_574bae65_fk_store_category_id` FOREIGN KEY (`category_id`) REFERENCES `store_category` (`id`);

--
-- Contraintes pour la table `store_productreview`
--
ALTER TABLE `store_productreview`
  ADD CONSTRAINT `store_productreview_product_id_28a58e2f_fk_store_product_id` FOREIGN KEY (`product_id`) REFERENCES `store_product` (`id`),
  ADD CONSTRAINT `store_productreview_user_id_7aa47bd8_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Contraintes pour la table `store_product_colors`
--
ALTER TABLE `store_product_colors`
  ADD CONSTRAINT `store_product_colors_color_id_24fc7ccb_fk_store_color_id` FOREIGN KEY (`color_id`) REFERENCES `store_color` (`id`),
  ADD CONSTRAINT `store_product_colors_product_id_25ad04c1_fk_store_product_id` FOREIGN KEY (`product_id`) REFERENCES `store_product` (`id`);

--
-- Contraintes pour la table `store_product_sizes`
--
ALTER TABLE `store_product_sizes`
  ADD CONSTRAINT `store_product_sizes_product_id_7a229b18_fk_store_product_id` FOREIGN KEY (`product_id`) REFERENCES `store_product` (`id`),
  ADD CONSTRAINT `store_product_sizes_size_id_fad63358_fk_store_size_id` FOREIGN KEY (`size_id`) REFERENCES `store_size` (`id`);

--
-- Contraintes pour la table `store_wishlist`
--
ALTER TABLE `store_wishlist`
  ADD CONSTRAINT `store_wishlist_product_id_8af1333d_fk_store_product_id` FOREIGN KEY (`product_id`) REFERENCES `store_product` (`id`),
  ADD CONSTRAINT `store_wishlist_user_id_afcc4e88_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
