package com.example.demo.controller;

import com.example.demo.dto.FileRequestDto;
import com.example.demo.service.DocumentService;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

@RestController
@RequestMapping("/api/documents")
public class DocumentController {

    private final DocumentService documentService;

    public DocumentController(DocumentService documentService) {
        this.documentService = documentService;
    }

    @PostMapping
    public ResponseEntity<String> uploadDocument(@RequestBody FileRequestDto request) {
        documentService.processDocument(request);
        return ResponseEntity.ok("Document processed successfully");
    }

    @GetMapping("/{fileName}")
    public ResponseEntity<String> getDocument(@PathVariable String fileName) {
        String content = documentService.readDocument(fileName);
        return ResponseEntity.ok(content);
    }
}
