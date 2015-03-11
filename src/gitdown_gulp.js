var gulp = require('gulp'),
    Gitdown = require('gitdown');

gulp.task('gitdown', function () {
    return Gitdown
        .read('.gitdown/README.md')
        .write('README.md');
});

gulp.task('watch', function () {
    gulp.watch(['./.gitdown/*'], ['gitdown']);
});
