-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Hôte : db
-- Généré le : mer. 17 mai 2023 à 08:57
-- Version du serveur : 8.0.33
-- Version de PHP : 8.1.18

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de données : `Binomontron`
--

-- --------------------------------------------------------

--
-- Structure de la table `Apprenants`
--

CREATE TABLE `Apprenants` (
  `id_apprenant` int NOT NULL,
  `nom` varchar(50) NOT NULL,
  `prenom` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `mail` varchar(70) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Déchargement des données de la table `Apprenants`
--

INSERT INTO `Apprenants` (`id_apprenant`, `nom`, `prenom`, `mail`) VALUES
(1, 'Frédéric', 'BOIREAU', 'frederic.boireau@isen-ouest.yncrea.fr'),
(2, 'Alexandre', 'CARAES', 'alexandre.caraes@isen-ouest.yncrea.fr'),
(4, 'Morgan', 'COULM', 'morgan.coulm@isen-ouest.yncrea.fr'),
(5, 'Andy', 'DUBIGNY', 'andy.dubigny@isen-ouest.yncrea.fr'),
(6, 'Youenn', 'FEULVARC’H', 'youenn.feulvarc-h@isen-ouest.yncrea.fr'),
(7, 'Pierre-Marie', 'GUEVEL', 'pierre-marie.guevel@isen-ouest.yncrea.fr'),
(8, 'Jérémy', 'LARDIC', 'jeremy.lardic@isen-ouest.yncrea.fr'),
(9, 'Ibrahim', 'MOHAMMAD', 'ibrahim.mohammad@isen-ouest.yncrea.fr'),
(10, 'Jonathan', 'NEEDHAM', 'jonathan.needham@isen-ouest.yncrea.fr'),
(11, 'Yves', 'PAUL', 'yves.paul@isen-ouest.yncrea.fr'),
(12, 'Laura', 'PERTRON', 'laura.pertron@isen-ouest.yncrea.fr'),
(13, 'Gwendal', 'QUENET', 'gwendal.quenet@isen-ouest.yncrea.fr'),
(14, 'Mickaël', 'RENNARD', 'mickael.rennard@isen-ouest.yncrea.fr'),
(15, 'Bastien', 'SUCHY-REINARD', 'bastien.suchy-reinard@isen-ouest.yncrea.fr'),
(16, 'Camille', 'ULVOAS', 'camille.ulvoas@isen-ouest.yncrea.fr');

-- --------------------------------------------------------

--
-- Structure de la table `App_Groupe`
--

CREATE TABLE `App_Groupe` (
  `id_apprenant` int NOT NULL,
  `id_groupe` int NOT NULL,
  `id_projet` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Structure de la table `Groupes`
--

CREATE TABLE `Groupes` (
  `id_groupe` int NOT NULL,
  `libelle` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `date` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Structure de la table `Projet`
--

CREATE TABLE `Projet` (
  `id_projet` int NOT NULL,
  `libelle` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `date_début` date NOT NULL,
  `date_fin` date NOT NULL,
  `id_groupe` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Index pour les tables déchargées
--

--
-- Index pour la table `Apprenants`
--
ALTER TABLE `Apprenants`
  ADD PRIMARY KEY (`id_apprenant`);

--
-- Index pour la table `App_Groupe`
--
ALTER TABLE `App_Groupe`
  ADD KEY `id_apprenant` (`id_apprenant`),
  ADD KEY `id_groupe` (`id_groupe`),
  ADD KEY `id_projet` (`id_projet`);

--
-- Index pour la table `Groupes`
--
ALTER TABLE `Groupes`
  ADD PRIMARY KEY (`id_groupe`);

--
-- Index pour la table `Projet`
--
ALTER TABLE `Projet`
  ADD PRIMARY KEY (`id_projet`),
  ADD KEY `id_groupe` (`id_groupe`);

--
-- AUTO_INCREMENT pour les tables déchargées
--

--
-- AUTO_INCREMENT pour la table `Apprenants`
--
ALTER TABLE `Apprenants`
  MODIFY `id_apprenant` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=22;

--
-- AUTO_INCREMENT pour la table `Groupes`
--
ALTER TABLE `Groupes`
  MODIFY `id_groupe` int NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT pour la table `Projet`
--
ALTER TABLE `Projet`
  MODIFY `id_projet` int NOT NULL AUTO_INCREMENT;

--
-- Contraintes pour les tables déchargées
--

--
-- Contraintes pour la table `App_Groupe`
--
ALTER TABLE `App_Groupe`
  ADD CONSTRAINT `App_Groupe_ibfk_1` FOREIGN KEY (`id_apprenant`) REFERENCES `Apprenants` (`id_apprenant`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  ADD CONSTRAINT `App_Groupe_ibfk_2` FOREIGN KEY (`id_groupe`) REFERENCES `Groupes` (`id_groupe`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  ADD CONSTRAINT `App_Groupe_ibfk_3` FOREIGN KEY (`id_projet`) REFERENCES `Projet` (`id_projet`) ON DELETE RESTRICT ON UPDATE RESTRICT;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
