-- Script gerado no MySQL Workbench


-- Criar tabela Cliente

CREATE TABLE `Cliente` (
  `idCliente` INT NOT NULL AUTO_INCREMENT,
  `Nome` VARCHAR(45) NOT NULL,
  `Tipo` ENUM('FISICA', 'JURIDICA') NOT NULL,
  `Identificacao` VARCHAR(20) NOT NULL,
  `Endereco` VARCHAR(45) NULL,
  `Clientecol` VARCHAR(45) NULL,
  PRIMARY KEY (`idCliente`)
);

-- Criar tabela Pedido

CREATE TABLE `Pedido` (
  `idPedido` INT NOT NULL,
  `Status` ENUM('EM ANDAMENTO', 'CONCLUIDO', 'CANCELADO') NOT NULL DEFAULT 'EM ANDAMENTO',
  `Observações` VARCHAR(45) NULL,
  `idCliente` INT NOT NULL,
  PRIMARY KEY (`idPedido`),
  CONSTRAINT `fk_Pedido_Cliente` FOREIGN KEY (`idCliente`) REFERENCES `Cliente` (`idCliente`)
);

-- Criar tabela Produto

CREATE TABLE `Produto` (
  `idProduto` INT NOT NULL,
  `Descrição` VARCHAR(45) NULL,
  `NCM` VARCHAR(45) NULL,
  PRIMARY KEY (`idProduto`)
);

-- Criar tabela relação Produto-Pedido

CREATE TABLE `Produto_Pedido` (
  `idPedido` INT NOT NULL,
  `idVendedor` INT NOT NULL,
  `idProduto` INT NOT NULL,
  `Quantidade` INT NULL,
  PRIMARY KEY (`idPedido`, `idVendedor`, `idProduto`),
  CONSTRAINT `fk_Pedido` FOREIGN KEY (`idPedido`) REFERENCES `Pedido` (`idPedido`),
  CONSTRAINT `fk_Vendedor` FOREIGN KEY (`idVendedor`) REFERENCES `Vendedor_Produto` (`idVendedor`),
  CONSTRAINT `fk_Produto`  FOREIGN KEY (`idProduto`) REFERENCES `Vendedor_Produto` (`idProduto`)
);

-- Criar tabela Vendedor

CREATE TABLE IF NOT EXISTS `Vendedor` (
  `idVendedor` INT NOT NULL,
  `Nome` VARCHAR(45) NULL,
  `Tipo` VARCHAR(45) NULL,
  `CPF / CNPJ` VARCHAR(45) NULL,
  PRIMARY KEY (`idVendedor`)
 );

-- Criar tabela Vendedor_Produto

CREATE TABLE `Vendedor_Produto` (
  `idVendedor` INT NOT NULL,
  `idProduto` INT NOT NULL,
  `Preço` FLOAT NULL,
  PRIMARY KEY (`Vendedor_idVendedor`, `Produto_idProduto`),
  CONSTRAINT `fk_Vendedor_Produto` FOREIGN KEY (`idVendedor`) REFERENCES `Vendedor` (`idVendedor`),
  CONSTRAINT `fk_Produto_Vendedor` FOREIGN KEY (`Produto_idProduto`) REFERENCES `Produto` (`idProduto`)
)