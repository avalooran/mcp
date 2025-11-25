package com.example.demo.service;

import com.example.demo.dto.FileRequestDto;
import org.springframework.stereotype.Service;
import test.sample.project.filemanager.FileManager;
import test.sample.project.logger.Logger;
import test.sample.project.secrets.SecretsManager;

@Service
public class DocumentService {

    private final FileManager fileManager;
    private final Logger logger;
    private final SecretsManager secretsManager;

    public DocumentService(FileManager fileManager, Logger logger, SecretsManager secretsManager) {
        this.fileManager = fileManager;
        this.logger = logger;
        this.secretsManager = secretsManager;
    }

    public void processDocument(FileRequestDto request) {
        logger.info("Starting document processing for: " + request.getFileName());

        // Example: Validate API Key before processing
        String apiKey = secretsManager.get("API_KEY");
        if (apiKey == null || apiKey.isEmpty()) {
            logger.error("API Key missing. Aborting.");
            throw new RuntimeException("Security violation: Missing API Key");
        }

        try {
            // Write content to file
            fileManager.write(request.getFileName(), request.getContent());
            logger.info("Successfully wrote file: " + request.getFileName());
        } catch (Exception e) {
            logger.error("Failed to write file: " + e.getMessage());
            throw e;
        }
    }
    
    public String readDocument(String fileName) {
        logger.info("Reading document: " + fileName);
        return fileManager.read(fileName);
    }
}
