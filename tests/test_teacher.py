import os
import logging
import unittest
from src.kdistiller import teacher

import torch 
import torch.nn as nn
from torch.utils.data import DataLoader, TensorDataset
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split


class TestTeacher(unittest.TestCase):
    def test_positive(self):
        n_features = 4
        n_classes = 5
        weights = [0.75, 0.1, 0.05, 0.08, 0.02]

        X, y = make_classification(n_samples=100, 
                                    n_features = n_features, 
                                    n_redundant = 0,
                                    n_classes=n_classes, 
                                    n_clusters_per_class=1,
                                    n_informative=3, 
                                    class_sep = 1,
                                    random_state=123,
                                    weights=weights)
        strat_val = y 
        X_train, X_validation, y_train, y_validation = train_test_split(
            X, y, test_size=0.2, stratify=strat_val, random_state=123)
        
        train_dataset = TensorDataset(torch.tensor(X_train, dtype=torch.float32),
                                    torch.tensor(y_train, dtype=torch.long))
        validation_dataset = TensorDataset(torch.tensor(X_validation, dtype=torch.float32),
                                            torch.tensor(y_validation, dtype=torch.long))
        training_loader = DataLoader(train_dataset, batch_size=256, shuffle=True)
        validation_loader = DataLoader(validation_dataset, batch_size=256)


        model = nn.Sequential(nn.Linear(n_features, 5), 
                            nn.Tanh(), nn.Linear(5, n_classes)) 
        
        weights_loss = 1 / torch.tensor(weights) 
        loss_func = nn.CrossEntropyLoss(weights_loss.float())

        name = "Test run "
        
        train_config = teacher.TrainingConfig(model=model,
                                epochs=10,
                                loss_func=loss_func, 
                                training_loader=training_loader, 
                                validation_loader=validation_loader,
                                save_model=True,
                                save_path=os.path.join(os.getcwd(), "runs"),
                                model_name=name, 
                                classification_metrics = True,
                                class_names = ['A', 'B', 'C', 'D', 'E'],
                                progress_bar=False,
                                zip_result=True)
    
        logging.info(f"start training of model: {train_config.model_name}")
        result = teacher.train(train_config)

        assert result == 1


if __name__ == '__main__':
    unittest.main()
