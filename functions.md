# PyTorch Functions for AiLang MVP

## Overview

Caroci the recommended PyTorch functions to implement in the AiLang interpreter.

## Core Tensor Operations

### Important Functions

| Function | Use Case | AiLang Example |
|----------|----------|----------------|
| `torch.tensor()` | Create tensors from Python data | `t := .tensor <- ((1, 2, 3))` |
| `torch.zeros()` | Create zero-filled tensors | `z := .zeros <- (10, 5)` |
| `torch.ones()` | Create ones-filled tensors | `o := .ones <- (3, 3)` |
| `torch.randn()` | Create random normal tensors | `r := .randn <- (100, 50)` |
| `torch.arange()` | Create range tensors | `a := .arange <- (0, 10)` |

### Maybe

| Function | Use Case |
|----------|----------|
| `torch.linspace()` | Create linearly spaced tensors |
| `torch.rand()` | Create uniform random tensors |
| `torch.empty()` | Create uninitialized tensors |
| `torch.full()` | Create tensors filled with a value |
| `torch.eye()` | Create identity matrices |

---

## Data Manipulation

### Important Functions

| Function | Use Case | AiLang Example |
|----------|----------|----------------|
| `tensor.shape` | Get tensor dimensions | `s := data.shape` |
| `tensor.reshape()` | Reshape tensors | `reshaped <- data.reshape <- (10, 5)` |
| `torch.cat()` | Concatenate tensors | `combined <- .cat <- (tensor1, tensor2)` |

### Maybe

| Function | Use Case |
|----------|----------|
| `tensor.squeeze()` | Remove single dimensions |
| `tensor.unsqueeze()` | Add dimensions |
| `tensor.flatten()` | Flatten tensor to 1D |
| `tensor.repeat()` | Repeat tensor elements |
| `tensor.expand()` | Expand tensor to new shape |
| `torch.split()` | Split tensor into chunks |

---

## Mathematical Operations(maybe)

### Important Functions

| Function | Use Case | AiLang Example |
|----------|----------|----------------|
| `torch.add()` / `+` | Element-wise addition | `result <- tensor1 + tensor2` |
| `torch.sub()` / `-` | Element-wise subtraction | `result <- tensor1 - tensor2` |
| `torch.mul()` / `*` | Element-wise multiplication | `result <- tensor1 * tensor2` |
| `torch.div()` / `/` | Element-wise division | `result <- tensor1 / tensor2` |
| `torch.matmul()` / `@` | Matrix multiplication | `result <- matrix1 @ matrix2` |

### Maybe

| Function | Use Case |
|----------|----------|
| `torch.sum()` | Sum reduction |
| `torch.mean()` | Mean reduction |
| `torch.std()` | Standard deviation |
| `torch.var()` | Variance |
| `torch.abs()` | Absolute value |
| `torch.sqrt()` | Square root |
| `torch.exp()` | Exponential |
| `torch.log()` | Natural logarithm |
| `torch.sin()` | Sine |
| `torch.cos()` | Cosine |
| `torch.pow()` | Power operation |
| `torch.min()` | Minimum value |
| `torch.max()` | Maximum value |

---

## Comparison & Filtering

### Important Functions

| Function | Use Case | AiLang Example |
|----------|----------|----------------|
| `torch.eq()` / `==` | Element-wise equality | `mask := tensor1 == tensor2` |
| `torch.gt()` / `>` | Greater than | `mask := tensor > 5` |
| `torch.lt()` / `<` | Less than | `mask := tensor < 10` |
| `torch.where()` | Conditional selection | `result <- .where <- (condition, x, y)` |

---

## Neural Network Layers

### Important Functions

| Function | Use Case | AiLang Example |
|----------|----------|----------------|
| `torch.nn.Linear()` | Fully connected layer | `layer := .Linear <- (in_features=784, out_features=128)` |
| `torch.nn.ReLU()` | ReLU activation | `activation := .ReLU` |
| `torch.nn.Sigmoid()` | Sigmoid activation | `activation := .Sigmoid` |
| `torch.nn.Softmax()` | Softmax activation | `activation := .Softmax <- (dim=1)` |
| `torch.nn.Conv2d()` | 2D convolution layer | `conv := .Conv2d <- (in_channels=3, out_channels=64, kernel_size=3)` |

### Maybe

| Function | Use Case |
|----------|----------|
| `torch.nn.Conv1d()` | 1D convolution |
| `torch.nn.Conv3d()` | 3D convolution |
| `torch.nn.MaxPool2d()` | 2D max pooling |
| `torch.nn.AvgPool2d()` | 2D average pooling |
| `torch.nn.Dropout()` | Dropout regularization |
| `torch.nn.BatchNorm1d()` | 1D batch normalization |
| `torch.nn.BatchNorm2d()` | 2D batch normalization |
| `torch.nn.LSTM()` | LSTM layer |
| `torch.nn.GRU()` | GRU layer |
| `torch.nn.Embedding()` | Embedding layer |

---

## Loss Functions

### Important Functions

| Function | Use Case | AiLang Example |
|----------|----------|----------------|
| `torch.nn.MSELoss()` | Mean squared error | `loss_fn := .MSELoss` |
| `torch.nn.CrossEntropyLoss()` | Cross entropy loss | `loss_fn := .CrossEntropyLoss` |
| `torch.nn.L1Loss()` | L1 (MAE) loss | `loss_fn := .L1Loss` |

---

## Optimizers

### Important Functions

| Function | Use Case | AiLang Example |
|----------|----------|----------------|
| `torch.optim.Adam()` | Adam optimizer | `optimizer := .Adam <- (model.parameters, lr=0.001)` |
| `torch.optim.SGD()` | Stochastic gradient descent | `optimizer := .SGD <- (model.parameters, lr=0.01, momentum=0.9)` |

---

## Gradient & Autograd

### Important Functions

| Function | Use Case |
|----------|----------|
| `tensor.backward()` | Compute gradients |
| `tensor.grad` | Access gradients |
| `torch.no_grad()` | Disable gradient tracking |
| `tensor.requires_grad_()` | Enable gradient tracking |
| `torch.autograd.grad()` | Compute specific gradients |

---

## Utility Functions

### Important Functions

| Function | Use Case |
|----------|----------|
| `torch.save()` | Save model/tensor to file |
| `torch.load()` | Load model/tensor from file |
| `len(tensor)` | Get size of first dimension |
| `tensor.item()` | Extract scalar value |
| `tensor.tolist()` | Convert to Python list |

### Example: Complete ML Workflow

```ailang
// Phase 1: Load and prepare data
from "train.csv" -> train_data
X := train_data.@features
y := train_data.target

// Phase 2: Create model
model := .Sequential <- (
    .Linear <- (784, 128),
    .ReLU,
    .Linear <- (128, 10)
)

// Phase 2: Loss and optimizer
loss_fn := .CrossEntropyLoss
optimizer := .Adam <- (model.parameters, lr=0.001)

// Phase 2: Training loop
do {
    // Forward pass
    output <- model <- (X)
    loss <- loss_fn <- (output, y)
    
    // Backward pass
    optimizer.zero_grad
    loss.backward
    optimizer.step
    
} if {
    epoch < 100
}

// Phase 2: Evaluation
predictions <- model <- (X_test)
accuracy <- .accuracy_score <- (y_test, predictions)