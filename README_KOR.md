# Microbiome Analysis
[ENGLISH](https://github.com/Kjamm/microbiome_analysis) [한국어](https://github.com/Kjamm/microbiome_analysis/blob/main/README_KOR.md)

이 라이브러리는 충남대학교 김재민의 개인적인 호기심으로 만들어졌습니다.

미생물군 데이터 분석을 위한 종합적인 Python 라이브러리로, 데이터 처리, Quality Control, 정규화, 다양성 분석, 시각화, 네트워크 분석 및 통계 비교 기능을 제공합니다.

## 기능

- **데이터 입력 및 변환**: 다양한 파일 형식(CSV, Excel, FASTQ, FASTA)을 지원하며 메타데이터와 시퀀스 데이터를 통합합니다.
- **Quality Control**: 시퀀스 Quality Control, 필터링 및 샘플 간 일관성 검사를 수행합니다.
- **정규화 및 필터링**: 샘플 크기 정규화, 희귀 시퀀스 제거 및 배경 잡음 필터링을 지원합니다.
- **다양성 분석**: 다양한 알파 및 베타 다양성 지표를 계산합니다.
- **분류**: 사전 학습된 분류기를 사용하여 시퀀스를 분류합니다.
- **시각화**: 다양성 지표, PCA/PCoA/NMDS 결과 및 네트워크 시각화를 제공합니다.
- **네트워크 분석**: 공존 네트워크 생성 및 중심성 분석을 수행합니다.
- **통계 분석**: ANOVA, PERMANOVA, 차등 풍부도 분석 및 상관 분석을 지원합니다.
- **대시보드**: 데이터 시각화 및 탐색을 위한 Streamlit 기반 대시보드를 제공합니다.

## 설치

라이브러리를 설치하려면 다음 명령어를 사용하십시오:

```bash
pip install microbiome_analysis
```

## 사용 예제
아래는 라이브러리의 다양한 기능을 사용하는 예제입니다.

## 데이터 입력 및 변환

```python
from microbiome_analysis import preprocessing

# FASTQ 파일에서 시퀀스 읽기
sequences = preprocessing.read_fastq("example.fastq")

# CSV 파일에서 메타데이터 읽기
metadata_df = preprocessing.read_csv("metadata.csv")

# 메타데이터와 시퀀스 데이터 병합
merged_data = preprocessing.merge_metadata_sequence(metadata_df, sequences)
```

## Quality Control
```python
from microbiome_analysis import qc

# 시퀀스 quality control 수행
qualities = qc.quality_control(sequences)

# quality control 분포 시각화
qc.plot_quality_distribution(sequences)

# 샘플 간 일관성 검사
samples = [sequences, sequences]  # 예제 샘플 목록
consistency = qc.check_consistency(samples)
print(f"샘플 간 일관성: {consistency}")
```

## 정규화 및 필터링
```python
from microbiome_analysis import normalization

# 샘플 크기 정규화
normalized_data = normalization.normalize_sample_size(data)

# 희귀 시퀀스 제거
filtered_data = normalization.remove_rare_sequences(data, threshold=10)

# 배경 잡음 필터링
cleaned_data = normalization.filter_background_noise(data, noise_threshold=0.01)
```

## 다양성 분석
```python
from microbiome_analysis import diversity

# 알파 다양성 지표 계산
alpha_diversity = diversity.calculate_alpha_diversity(data)
print(alpha_diversity)
```

## 베타 다양성 분석
```python
from microbiome_analysis import beta_diversity

# PCA 분석 수행
pca_coords = beta_diversity.pca_analysis(data)

# PCoA 분석 수행
pcoa_coords = beta_diversity.pcoa_analysis(data)

# NMDS 분석 수행
nmds_coords = beta_diversity.nmds_analysis(data)
```

## 분류
```python
from microbiome_analysis import classification

# 분류기 학습
sequences = [
    'ATCGGCTAAG',
    'GCTTAGCTAG',
    'TTCGCTGATC',
    'GCTAGCTAGT'
]
labels = [
    'species_1',
    'species_2',
    'species_1',
    'species_2'
]
trained_classifier = classification.train_classifier(sequences, labels)

# 새로운 샘플 분류
new_samples = [
    'ATCGGCTAAG',
    'GCTAGCTAGT'
]
predicted_labels = classification.classify_new_samples(new_samples, trained_classifier)
print(predicted_labels)
```

## 시각화
```python
from microbiome_analysis import visualization

# 알파 다양성 지표 시각화
visualization.plot_alpha_diversity(alpha_diversity)

# PCA 결과 시각화
visualization.plot_pca(pca_coords, labels)

# 베타 다양성 결과 시각화
visualization.plot_beta_diversity(pcoa_coords, method='PCoA')
```

## 네트워크 분석
```python
from microbiome_analysis import network

# 공존 네트워크 생성
cooccurrence_network = network.create_cooccurrence_network(data)

# 네트워크 시각화
network.plot_network(cooccurrence_network)

# 네트워크 중심성 분석
centrality = network.analyze_network_centrality(cooccurrence_network)
print(centrality)
```

## 통계 분석
```python
from microbiome_analysis import statistics

# ANOVA 분석 수행
anova_result = statistics.anova_analysis(groups)
print(anova_result)

# PERMANOVA 분석 수행
permanova_result = statistics.perm_anova(data, groups)
print(permanova_result)

# 상관 분석 수행
correlation_result = statistics.correlation_analysis(data1, data2, method='spearman')
print(correlation_result)
```

## 대시보드
```python
from microbiome_analysis import dashboard

# 대시보드 생성
data = pd.DataFrame({
    'feature1': [10, 20, 30],
    'feature2': [20, 30, 40]
})
diversity_df = pd.DataFrame({
    'shannon': [1.0, 2.0, 3.0],
    'simpson': [0.5, 0.3, 0.2]
})
pca_coords = pd.DataFrame({
    'PC1': [1.0, 2.0, 3.0],
    'PC2': [0.5, 0.3, 0.2]
})
labels = ['label1', 'label2', 'label3']
dashboard.create_dashboard(data, diversity_df, pca_coords, labels)
```

## 기여
기여는 언제나 환영입니다! 버그나 기능 요청을 위해 Pull Request를 제출하거나 Issue를 열어주세요.

## 라이선스
이 프로젝트는 MIT 라이선스를 따릅니다.
