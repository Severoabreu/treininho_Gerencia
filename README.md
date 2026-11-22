# ATIVIDADE AVALIATIVA 2ª UNIDADE

## **Domínio**

Escolha uma entidade em substituição a entidade Tarefa. Substitua os atribuitos de acordo.

## **1. Requisitos funcionais**

### **RF01 — Cadastrar tarefa**

O usuário poderá cadastrar uma nova tarefa informando seu título e sua descrição. Durante o cadastro, o título deverá ser preenchido obrigatoriamente e não poderá conter apenas espaços em branco. A descrição será opcional, permitindo que o usuário registre tarefas com diferentes níveis de detalhamento.

Toda tarefa deverá ser registrada inicialmente com a situação **pendente**, independentemente das informações fornecidas pelo usuário. Após a operação, o sistema deverá informar se o cadastro foi realizado com sucesso e disponibilizar o identificador atribuído à tarefa.

### **RF02 — Listar tarefas**

O usuário poderá consultar a relação de todas as tarefas cadastradas no sistema, independentemente de estarem concluídas ou pendentes. Para cada tarefa, deverão ser apresentados seu identificador, título, descrição e situação atual.

As tarefas deverão ser exibidas de maneira organizada e legível no terminal, facilitando a identificação e o acompanhamento das atividades. Caso não existam tarefas cadastradas, o sistema deverá apresentar uma mensagem informando que não há registros disponíveis.

### **RF03 — Consultar tarefa por identificador**

O usuário poderá consultar individualmente uma tarefa informando seu identificador. Quando o registro for encontrado, o sistema deverá apresentar todas as informações associadas à tarefa, incluindo título, descrição e situação atual.

Caso o identificador informado não corresponda a nenhuma tarefa cadastrada, o sistema deverá comunicar que o registro não foi encontrado, evitando apresentar informações incorretas ou interromper a execução da aplicação.

### **RF04 — Atualizar tarefa**

O usuário poderá modificar as informações de uma tarefa previamente cadastrada, utilizando seu identificador para localizar o registro que deseja alterar.

A operação permitirá atualizar o título e a descrição da tarefa. O título continuará sendo obrigatório e deverá respeitar as mesmas regras de validação aplicadas durante o cadastro. A atualização dessas informações não deverá modificar a situação da tarefa, preservando seu estado atual de conclusão ou pendência.

Após a operação, o sistema deverá informar se a atualização foi realizada com sucesso. Caso a tarefa não seja encontrada, deverá apresentar uma mensagem adequada ao usuário.

### **RF05 — Excluir tarefa**

O usuário poderá excluir uma tarefa cadastrada informando seu identificador. Antes de efetivar a exclusão, o sistema deverá solicitar uma confirmação, permitindo que o usuário desista da operação.

Quando confirmada, a tarefa deverá ser removida permanentemente do banco de dados e deixar de aparecer nas consultas e listagens posteriores. Caso o usuário cancele a operação, nenhuma alteração deverá ser realizada.

Se o identificador informado não corresponder a uma tarefa existente, o sistema deverá apresentar uma mensagem informativa, sem provocar erros na aplicação.

### **RF06 — Concluir tarefa**

O usuário poderá marcar uma tarefa pendente como concluída, informando seu identificador. O sistema deverá localizar o registro e alterar seu atributo de situação para indicar que a atividade foi finalizada.

Após a alteração, a nova situação deverá ser persistida no banco de dados e apresentada ao usuário como confirmação da operação. Caso o identificador não corresponda a uma tarefa cadastrada, o sistema deverá informar que não foi possível localizar o registro.

### **RF07 — Reabrir tarefa**

O usuário poderá reabrir uma tarefa que já tenha sido concluída, informando seu identificador. Essa operação deverá modificar a situação da tarefa de concluída para pendente, permitindo que ela volte a ser acompanhada como uma atividade ainda não finalizada.

A alteração deverá ser persistida no banco de dados e refletida nas consultas e listagens posteriores. Caso a tarefa não seja encontrada, o sistema deverá apresentar uma mensagem informativa ao usuário.

## **2. Funcionalidades**

Cada funcionalidade deverá ser desenvolvida individualmente, respeitando a arquitetura em camadas do projeto. O desenvolvimento deverá contemplar as alterações necessárias nas entidades, serviços, repositórios e interfaces, conforme a responsabilidade de cada componente.

### **Feature 1 — Cadastro de tarefas**

RF01

O desenvolvimento deverá contemplar:

1. Implementação ou adequação da entidade `Task`, contemplando seus atributos e a representação de uma nova tarefa.
2. Implementação da operação de persistência no `TaskRepository`, incluindo a inserção dos dados no banco SQLite e a recuperação do identificador gerado.
3. Implementação das regras de cadastro no `TaskService`, incluindo a validação do título e a definição da situação inicial como pendente.
4. Integração da funcionalidade à interface de terminal, permitindo que o usuário informe os dados e receba o resultado do cadastro.

**Resultado esperado:** o usuário consegue cadastrar tarefas e visualizar a confirmação da operação, com os dados armazenados corretamente no banco.

### **Feature 2 — Listagem de tarefas**

RF02

O desenvolvimento deverá contemplar:

1. Implementação da consulta de todas as tarefas no `TaskRepository`, recuperando os registros armazenados no banco de dados.
2. Implementação da operação de listagem no `TaskService`, organizando os dados retornados pelo repositório.
3. Implementação da apresentação das tarefas no `TaskMenu`, exibindo identificador, título, descrição e situação.
4. Tratamento da situação em que não existem tarefas cadastradas, apresentando uma mensagem adequada ao usuário.

**Resultado esperado:** o usuário consegue visualizar todas as tarefas cadastradas e identificar facilmente quais estão pendentes e quais foram concluídas.

### **Feature 3 — Consulta de tarefa por identificador**

RF03

O desenvolvimento deverá contemplar:

1. Implementação da consulta de uma tarefa específica pelo identificador no `TaskRepository`.
2. Implementação da operação de consulta no `TaskService`, tratando os casos em que o registro não existe.
3. Implementação da interação no `TaskMenu`, solicitando o identificador e apresentando os dados da tarefa encontrada.
4. Tratamento de identificadores inválidos ou inexistentes, evitando interrupções inesperadas na aplicação.

**Resultado esperado:** o usuário consegue localizar e visualizar individualmente uma tarefa por meio de seu identificador.

### **Feature 4 — Atualização de tarefas**

RF04

O desenvolvimento deverá contemplar:

1. Implementação da operação de atualização no `TaskRepository`, permitindo modificar o título e a descrição de uma tarefa existente.
2. Implementação das regras de atualização no `TaskService`, incluindo validação do título e verificação da existência da tarefa.
3. Garantia de que a atualização dos dados descritivos preserve a situação atual da tarefa.
4. Implementação da interação no `TaskMenu`, permitindo informar o identificador e os novos dados da tarefa.

**Resultado esperado:** o usuário consegue modificar as informações de uma tarefa sem alterar indevidamente seu estado de conclusão.

### **Feature 5 — Exclusão de tarefas**

RF05

O desenvolvimento deverá contemplar:

1. Implementação da operação de exclusão no `TaskRepository`, removendo do banco de dados a tarefa identificada.
2. Implementação das regras de exclusão no `TaskService`, incluindo a verificação da existência do registro.
3. Implementação da solicitação de confirmação na interface, permitindo confirmar ou cancelar a operação.
4. Apresentação de mensagens adequadas para os casos de exclusão realizada, cancelamento ou tarefa inexistente.

**Resultado esperado:** o usuário consegue excluir tarefas de maneira controlada, com confirmação prévia e persistência correta da exclusão.

### **Feature 6 — Concluir tarefa**

RF06

O desenvolvimento deverá contemplar:

1. Implementação da operação de alteração do atributo `completed` no `TaskRepository`, permitindo registrar uma tarefa como concluída.
2. Implementação da regra de conclusão no `TaskService`, verificando a existência da tarefa antes de alterar sua situação.
3. Integração da operação à interface de terminal, permitindo que o usuário informe o identificador da tarefa que deseja concluir.
4. Apresentação de mensagens de confirmação ou de erro, conforme o resultado da operação.

**Resultado esperado:** o usuário consegue marcar tarefas como concluídas e consultar posteriormente a situação atualizada.

### **Feature 7 — Reabrir tarefa**

RF07

O desenvolvimento deverá contemplar:

1. Implementação da operação de alteração do atributo `completed` no `TaskRepository`, permitindo retornar uma tarefa ao estado pendente.
2. Implementação da regra de reabertura no `TaskService`, verificando a existência da tarefa antes de realizar a alteração.
3. Integração da operação à interface de terminal, permitindo que o usuário selecione a tarefa que deseja reabrir.
4. Apresentação de mensagens de confirmação ou de erro, conforme o resultado da operação.

**Resultado esperado:** o usuário consegue reabrir tarefas anteriormente concluídas, permitindo que voltem a ser acompanhadas como pendentes.
