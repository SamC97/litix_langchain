import Levenshtein
from jiwer import wer, cer
from src.utils.text_utils import clean_text_value

def compute_precision(groundtruth: dict, prediction: dict) -> float:
    """
    Calculate precision as:
      (# of correctly predicted fields) / (# of fields predicted)
    
    A field is considered correctly predicted if its cleaned value exactly matches 
    the corresponding groundtruth value.
    """
    true_positive = 0
    false_positive = 0

    # Loop over the predicted keys
    for key, pred_value in prediction.items():
        gt_value = groundtruth.get(key)
        if gt_value is not None:
            # Clean the strings (strip whitespace and lower-case)
            cleaned_gt = clean_text_value(gt_value)
            cleaned_pred = clean_text_value(pred_value)
            if cleaned_gt == cleaned_pred:
                true_positive += 1
            else:
                false_positive += 1
        else:
            false_positive += 1

    if (true_positive + false_positive) == 0:
        return 0.0
    return true_positive / (true_positive + false_positive)


def compute_recall(groundtruth: dict, prediction: dict) -> float:
    """
    Calculate recall as:
      (# of correctly predicted fields) / (# of fields in groundtruth)
    
    A field is considered correctly predicted if its cleaned value exactly matches 
    the corresponding groundtruth value.
    """
    true_positive = 0
    false_negative = 0

    # Loop over all groundtruth keys
    for key, gt_value in groundtruth.items():
        pred_value = prediction.get(key)
        if pred_value is not None:
            # Clean the strings
            cleaned_gt = clean_text_value(gt_value)
            cleaned_pred = clean_text_value(pred_value)
            if cleaned_gt == cleaned_pred:
                true_positive += 1
            else:
                false_negative += 1
        else:
            false_negative += 1

    if (true_positive + false_negative) == 0:
        return 0.0
    return true_positive / (true_positive + false_negative)


def compute_f1(groundtruth: dict, prediction: dict) -> float:
    """
    Calculate the F1 score as the harmonic mean of precision and recall.
    """
    precision = compute_precision(groundtruth, prediction)
    recall = compute_recall(groundtruth, prediction)
    if (precision + recall) == 0:
        return 0.0
    return 2 * precision * recall / (precision + recall)


def compute_cer(reference: str, hypothesis: str) -> float:
    """
    Calculate the Character Error Rate (CER) between two strings.
    
    Parameters:
        reference (str): The reference string.
        hypothesis (str): The hypothesis string.
    
    Returns:
        float: The CER between the two strings.
    """
    cleaned_reference = clean_text_value(reference)
    cleaned_hypothesis = clean_text_value(hypothesis)
    print(f"Comparing '{cleaned_reference}' and '{cleaned_hypothesis}' for CER")
    return cer(cleaned_reference, cleaned_hypothesis)


def compute_wer(reference: str, hypothesis: str) -> float:
    """
    Calculate the Word Error Rate (WER) between two strings.
    
    Parameters:
        reference (str): The reference string.
        hypothesis (str): The hypothesis string.
    
    Returns:
        float: The WER between the two strings.
    """
    cleaned_reference = clean_text_value(reference)
    cleaned_hypothesis = clean_text_value(hypothesis)
    return wer(cleaned_reference, cleaned_hypothesis)


def compute_levenshtein_distance(reference: str, hypothesis: str) -> float:
    """
    Calculates the Levenshtein distance between two strings. (not the similarity)
    
    Parameters:
        reference (str): The reference string.
        hypothesis (str): The hypothesis string.
    
    Returns:
        float: Distance score between 0.0 and 1.0.
    """
    cleaned_reference = clean_text_value(reference)
    cleaned_hypothesis = clean_text_value(hypothesis)
    if len(cleaned_reference) == 0 and len(cleaned_hypothesis) == 0:
        return 1.0
    dist = Levenshtein.distance(cleaned_reference, cleaned_hypothesis)
    return (dist / max(len(cleaned_reference), len(cleaned_hypothesis)))
